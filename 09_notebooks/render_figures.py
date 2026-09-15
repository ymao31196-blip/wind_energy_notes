from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt

FIG_DIR = Path(__file__).resolve().parent / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def cf_proxy(ws):
    ws = np.asarray(ws, dtype=float)
    out = np.zeros_like(ws)
    partial = (ws >= 3.0) & (ws < 12.0)
    rated = (ws >= 12.0) & (ws <= 25.0)
    out[partial] = ((ws[partial] - 3.0) / 9.0) ** 3
    out[rated] = 1.0
    return out


# 1. Same mean, different wind-speed distributions.
rng = np.random.default_rng(42)
target_mean = 7.0
n = 200_000
k_a, k_b = 2.0, 5.0
c_a = target_mean / math.gamma(1.0 + 1.0 / k_a)
c_b = target_mean / math.gamma(1.0 + 1.0 / k_b)
ws_a = c_a * rng.weibull(k_a, n)
ws_b = c_b * rng.weibull(k_b, n)

bins = np.linspace(0, 20, 60)
plt.figure(figsize=(8, 4.5))
plt.hist(ws_a, bins=bins, density=True, alpha=0.5, label=f"A: k={k_a}")
plt.hist(ws_b, bins=bins, density=True, alpha=0.5, label=f"B: k={k_b}")
plt.xlabel("Wind speed (m/s)")
plt.ylabel("Probability density")
plt.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "wind_distribution_comparison.png", dpi=180)
plt.close()

# 2. CF proxy curve.
x = np.linspace(0, 30, 500)
plt.figure(figsize=(8, 4.5))
plt.plot(x, cf_proxy(x))
plt.xlabel("Wind speed (m/s)")
plt.ylabel("CF proxy")
plt.tight_layout()
plt.savefig(FIG_DIR / "cf_proxy_curve.png", dpi=180)
plt.close()

# 3. Vector components under changing direction.
hours_total = 30 * 24
speed = np.full(hours_total, 8.0)
theta = np.linspace(0, 2 * np.pi, hours_total, endpoint=False)
u = speed * np.cos(theta)
v = speed * np.sin(theta)
hours = np.arange(168)
plt.figure(figsize=(9, 4.5))
plt.plot(hours, u[:168], label="u")
plt.plot(hours, v[:168], label="v")
plt.xlabel("Hour")
plt.ylabel("Wind component (m/s)")
plt.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "vector_components_week.png", dpi=180)
plt.close()

# 4. Aggregation order.
ws_grid = np.array([
    [2.0, 4.0, 6.0, 8.0],
    [3.0, 5.0, 9.0, 12.0],
    [4.0, 7.0, 10.0, 14.0],
])
route_a = cf_proxy(ws_grid).mean()
route_b = float(cf_proxy(np.array([ws_grid.mean()]))[0])
plt.figure(figsize=(6, 4.5))
plt.bar(["mean[CF(ws)]", "CF(mean[ws])"], [route_a, route_b])
plt.ylabel("CF proxy")
plt.tight_layout()
plt.savefig(FIG_DIR / "aggregation_order_comparison.png", dpi=180)
plt.close()

# 5. MCP reconstruction.
rng = np.random.default_rng(7)
months = np.arange(20 * 12)
season = 1.3 * np.sin(2 * np.pi * months / 12.0)
reference = 6.5 + season + rng.normal(0, 0.8, size=months.size)
site_true = 1.0 + 0.88 * reference + rng.normal(0, 0.45, size=months.size)
overlap_start = 8 * 12
overlap_end = 10 * 12
mask = (months >= overlap_start) & (months < overlap_end)
coef = np.polyfit(reference[mask], site_true[mask], deg=1)
site_reconstructed = np.polyval(coef, reference)
years = 2000 + months / 12.0
plt.figure(figsize=(10, 4.5))
plt.plot(years, site_true, label="synthetic site truth", linewidth=1)
plt.plot(years, site_reconstructed, label="MCP reconstruction", linewidth=1)
plt.axvspan(2000 + overlap_start / 12.0, 2000 + overlap_end / 12.0, alpha=0.15, label="overlap period")
plt.xlabel("Year")
plt.ylabel("Wind speed (m/s)")
plt.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "mcp_long_term_reconstruction.png", dpi=180)
plt.close()

# 6. Monte Carlo AEP uncertainty distribution.
rng = np.random.default_rng(2026)
n_mc = 20_000
n_wind = 50_000
shape_k = 2.2
target_mean = 7.5
scale_c = target_mean / math.gamma(1.0 + 1.0 / shape_k)
base_ws = scale_c * rng.weibull(shape_k, n_wind)

wind_scale = rng.normal(loc=1.0, scale=0.03, size=n_mc)
wake_loss = np.clip(rng.normal(loc=0.08, scale=0.02, size=n_mc), 0.0, 0.30)
availability_loss = np.clip(rng.normal(loc=0.03, scale=0.01, size=n_mc), 0.0, 0.15)
electrical_loss = np.clip(rng.normal(loc=0.02, scale=0.005, size=n_mc), 0.0, 0.10)

scale_grid = np.linspace(0.88, 1.12, 301)
cf_grid = np.array([cf_proxy(base_ws * s).mean() for s in scale_grid])
gross_cf = np.interp(wind_scale, scale_grid, cf_grid)
net_cf = (
    gross_cf
    * (1.0 - wake_loss)
    * (1.0 - availability_loss)
    * (1.0 - electrical_loss)
)
aep_proxy = net_cf * 8760.0
p50 = np.percentile(aep_proxy, 50)
p90 = np.percentile(aep_proxy, 10)

plt.figure(figsize=(8, 4.5))
plt.hist(aep_proxy, bins=70, density=True, alpha=0.75)
plt.axvline(p50, linestyle="--", label="P50")
plt.axvline(p90, linestyle="--", label="P90")
plt.xlabel("Net AEP proxy (full-load-hours)")
plt.ylabel("Probability density")
plt.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "aep_uncertainty_distribution.png", dpi=180)
plt.close()

# 7. Simplified wind-turbine control regions.
omega = np.linspace(0.2, 1.2, 500)
omega_rated = 1.0
torque = np.where(
    omega <= omega_rated,
    omega**2,
    1.0 / omega
)
power = torque * omega

plt.figure(figsize=(8, 4.5))
plt.plot(omega, torque, label="Generator torque")
plt.plot(omega, power, label="Electrical power")
plt.axvline(omega_rated, linestyle="--", label="Rated speed")
plt.xlabel("Normalized generator speed")
plt.ylabel("Normalized value")
plt.legend()
plt.tight_layout()
plt.savefig(FIG_DIR / "turbine_control_regions.png", dpi=180)
plt.close()

print(f"rendered {len(list(FIG_DIR.glob('*.png')))} figures to {FIG_DIR}")
