---
chunk_id: "satellite-communication-tutorial-organized-v2-12df00b892-chunk-0002"
source_id: "satellite-communication-tutorial-organized-v2-12df00b892"
source_file: "New folder (3)/Satellite_Communication_Tutorial_Organized_v2.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "Exams and Questions"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

Example 2: LEO Elliptical Orbit
Mean motion (n) = 14.23304826 rev/day, Eccentricity (e) = 0.0011501. 
Solution:
1. n = 1.04 × 10⁻³ rad/s.
2. Semi-major axis (a): 7169.522 km.
3. Apogee Height (ha): r_a = a(1+e) → ha = r_a - R = 806.768 km.
4. Perigee Height (hp): r_p = a(1-e) → hp = r_p - R = 790.276 km. 
Section 5: Quiz - Rain Attenuation and Noise
CME 574 Quiz 1:
Rain Attenuation = 4 dB (A = 2.512). Noise temps: T_ant = 100K, T_lna = 50K,
T_mixer = 10000K. System Temp (Ts) = 350K. 
Solution:
T_rain = 290 (1 - 1/2.512) = 174.55 K.
Ts = T_rain + T_ant + T_lna + (T_mixer / G_lna)
350 = 174.55 + 100 + 50 + (10000 / G_lna)
G_lna = 10000 / 25.45 = 392.9 → G_lna ≈ 25.94 dB.
Constants Reference
Earth Radius: 6,378 km
Kepler's Constant (μ): 3.986 × 10⁵ km³/s²
Velocity of light (c): 3 × 10⁸ m/s
GEO Height: 36,000 km
