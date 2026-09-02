#!/usr/bin/env python3
"""
OATMEAL-CRETE v1.0 — MOLD-RESISTANT BIOCOMPOSITE (~4 MPa TARGET)
OATMEAL • HYDRATED LIME • SAND • PARALLEL SALT BLEND

Interactive terminal guide:
- Calculates batch masses
- Guides oatmeal prep
- Guides salt blend prep
- Guides mixing, casting, and curing
"""

import sys
from textwrap import dedent

def pause(msg="Press ENTER to continue..."):
    input(f"\n{msg}\n")

def ask_float(prompt, default=None):
    while True:
        txt = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ").strip()
        if not txt and default is not None:
            return float(default)
        try:
            return float(txt)
        except ValueError:
            print("Please enter a number.")

def banner():
    print("=" * 70)
    print(" OATMEAL-CRETE v1.0 — MOLD-RESISTANT BIOCOMPOSITE GUIDE ")
    print("=" * 70)
    print(dedent("""
        Target:
          - ~4 MPa compressive strength (non-structural).
          - Strong resistance to mold via high pH + low sugars + salt blend.

        Base ratios (by mass):
          - Fine sand (0–2 mm):          4.0 parts
          - Hydrated lime:               2.7 parts
          - Dry oatmeal (flakes):        0.8 parts
          - Parallel salt blend:         0.20 parts
          - Water:                       1.6–2.0 parts (tuned to workability)

        Parallel salt blend (by mass):
          - NaCl:                        2 parts
          - CaCl₂:                       1 part
          - NaHCO₃:                      1 part
    """))

def choose_batch():
    print("\n--- BATCH SIZE SELECTION ---")
    print("Define the mass corresponding to '1 part' (e.g., 1 kg).")
    one_part = ask_float("Enter mass for 1 part (kg)", default=1.0)

    sand = 4.0 * one_part
    lime = 2.7 * one_part
    oatmeal = 0.8 * one_part
    salt_blend = 0.20 * one_part
    water_min = 1.6 * one_part
    water_max = 2.0 * one_part

    print("\n--- CALCULATED MATERIAL MASSES ---")
    print(f"Fine sand:        {sand:.3f} kg")
    print(f"Hydrated lime:    {lime:.3f} kg")
    print(f"Dry oatmeal:      {oatmeal:.3f} kg")
    print(f"Salt blend:       {salt_blend:.3f} kg")
    print(f"Water (start):    {water_min:.3f} kg")
    print(f"Water (max):      {water_max:.3f} kg")

    return {
        "one_part": one_part,
        "sand": sand,
        "lime": lime,
        "oatmeal": oatmeal,
        "salt_blend": salt_blend,
        "water_min": water_min,
        "water_max": water_max,
    }

def salt_breakdown(salt_blend_mass):
    print("\n--- PARALLEL SALT BLEND BREAKDOWN ---")
    print("Salt blend ratio: NaCl : CaCl₂ : NaHCO₃ = 2 : 1 : 1")

    total_parts = 2 + 1 + 1
    part_mass = salt_blend_mass / total_parts

    nacl = 2 * part_mass
    cacl2 = 1 * part_mass
    nahco3 = 1 * part_mass

    print(f"Total salt blend: {salt_blend_mass:.3f} kg")
    print(f"  NaCl:           {nacl:.3f} kg")
    print(f"  CaCl₂:          {cacl2:.3f} kg")
    print(f"  NaHCO₃:         {nahco3:.3f} kg")

    return {"nacl": nacl, "cacl2": cacl2, "nahco3": nahco3}

def oatmeal_prep_instructions(oatmeal_mass):
    print("\n=== STEP 1 — DRY OATMEAL PREPARATION ===")
    print(dedent(f"""
        Target dry oatmeal mass: {oatmeal_mass:.3f} kg

        Oatmeal prep (for mold resistance and strength):
          1. Use plain rolled oats (no sugar, no flavorings).
          2. Spread oats in a thin layer on trays.
          3. Dry at low heat (50–80 °C) or in a warm, ventilated area:
             - Goal: very dry, crisp flakes.
             - No residual moisture when squeezed.
          4. Optionally break into smaller flakes (2–8 mm).
          5. Store in a dry, breathable container until mixing.
    """))
    pause("Press ENTER when your oatmeal is prepared or you understand the prep steps...")

def salt_prep_instructions(salt_masses):
    print("\n=== STEP 2 — PARALLEL SALT BLEND PREPARATION ===")
    total = salt_masses["nacl"] + salt_masses["cacl2"] + salt_masses["nahco3"]
    print(dedent(f"""
        Target salt blend mass: {total:.3f} kg

        Weigh:
          - NaCl:   {salt_masses['nacl']:.3f} kg
          - CaCl₂:  {salt_masses['cacl2']:.3f} kg
          - NaHCO₃: {salt_masses['nahco3']:.3f} kg

        Steps:
          1. Combine all three in a dry container.
          2. Break up any lumps.
          3. Mix until visually uniform.
          4. Keep sealed and dry (CaCl₂ is hygroscopic).
    """))
    pause()

def dry_mix_instructions(batch):
    print("\n=== STEP 3 — DRY MIXING (SAND + LIME + SALT BLEND) ===")
    print(dedent(f"""
        Weigh:
          - Fine sand:        {batch['sand']:.3f} kg
          - Hydrated lime:    {batch['lime']:.3f} kg
          - Salt blend:       {batch['salt_blend']:.3f} kg

        Steps:
          1. Add sand and lime to your mixing tub or mortar mixer.
          2. Dry-mix 2–3 minutes until color is uniform.
          3. Sprinkle the salt blend evenly over the surface.
          4. Mix another 2–3 minutes.
          5. Goal: no visible pockets of lime or salt.
    """))
    pause()

def add_oatmeal_instructions(batch):
    print("\n=== STEP 4 — ADDING DRY OATMEAL ===")
    print(dedent(f"""
        Target dry oatmeal mass: {batch['oatmeal']:.3f} kg

        Steps:
          1. Add the dried oatmeal flakes to the dry mix.
          2. Fold and toss until all flakes are coated.
          3. Check a handful:
             - Oatmeal behaves like lightweight aggregate.
             - No large uncoated clumps.
    """))
    pause()

def hydration_instructions(batch):
    print("\n=== STEP 5 — HYDRATION & WORKABILITY (MOLD-RESISTANT) ===")
    print(dedent(f"""
        Initial water target:
          - Start with: {batch['water_min']:.3f} kg
          - Do not exceed: {batch['water_max']:.3f} kg without adjusting solids.

        NOTE:
          - Oatmeal absorbs water; the mix will stiffen over time.
          - Add water gradually and allow a few minutes between additions.

        Steps:
          1. Add water in 3–5 small increments.
          2. After each addition, mix 1–2 minutes.
          3. Desired consistency:
             - Stiff, cohesive.
             - Holds shape when squeezed in a gloved hand.
             - Slight surface sheen.
             - No free water pooling at the bottom.

        If too dry and crumbly:
          - Add water in small increments (e.g., 0.1–0.2 kg).

        If too soupy:
          - Add small amounts of sand and lime (maintain ~2.7:4.0 lime:sand ratio).
    """))
    pause()

def casting_instructions():
    print("\n=== STEP 6 — CASTING INTO MOLDS ===")
    print(dedent("""
        Recommended molds:
          - 50 mm cubes or cylinders for compressive tests.
          - Larger blocks/panels for practical evaluation.

        Steps:
          1. Prepare molds:
             - Clean.
             - Lightly oil or apply release agent compatible with lime-based mixes.
          2. Fill molds in 2–3 lifts:
             - Place material.
             - Lightly tamp each lift to remove large voids.
             - Avoid heavy vibration or over-compaction.
          3. Strike off the top flush with mold edges.
          4. Optionally trowel smooth or leave textured.
    """))
    pause()

def curing_instructions():
    print("\n=== STEP 7 — CURING REGIME FOR MOLD RESISTANCE ===")
    print(dedent("""
        PHASE 1 — INITIAL SET (0–24 HOURS):
          - Keep molds in shaded, ventilated area.
          - Cover loosely (plastic sheet or damp cloth) to prevent rapid surface drying.
          - Avoid direct sun and strong wind.

        PHASE 2 — EARLY CURE (DAY 1–7):
          - Demold after 24–48 hours if firm.
          - Place specimens on racks with airflow.
          - Maintain moderate humidity:
            - Nearby water trays or light misting of surrounding air.
          - Do NOT soak the specimens.
          - Goal: even drying, no trapped wet pockets.

        PHASE 3 — MAIN CURE (DAY 7–28):
          - Store in dry, ventilated environment.
          - Avoid immersion or heavy wetting.
          - Lime binder needs CO₂ from air for carbonation.

        OPTIONAL — POST-28-DAY SEALER:
          - After at least 28 days of cure:
            - Apply a breathable mineral/silicate sealer to all faces.
            - Goal: block liquid water, allow CO₂ for ongoing carbonation.
    """))
    pause()

def testing_instructions():
    print("\n=== STEP 8 — TESTING & ADJUSTMENT TOWARD ~4 MPa ===")
    print(dedent("""
        TESTING:
          - At 7 days:
            - Perform preliminary compressive tests (expect <4 MPa).
          - At 28 days:
            - Perform main compressive tests.
            - Record:
              - Failure load.
              - Failure mode (brittle, shear, etc.).
              - Density (mass/volume).

        ADJUSTMENT RULES:
          If strength <4 MPa:
            - Increase mineral fraction slightly:
              - Sand: 4.2 parts
              - Lime: 2.8 parts
              - Oatmeal: 0.7 parts
            - Keep salt blend near 0.20 parts.

          If mix is too brittle:
            - Increase oatmeal slightly:
              - Oatmeal: 0.9 parts
              - Sand: 3.8 parts
            - Keep lime around 2.7 parts.

          If excessive salt efflorescence:
            - Reduce salt blend to ~0.15 parts.

        SAFETY:
          - Wear gloves, mask, and eye protection.
          - Avoid inhaling dust from lime, sand, and salts.
          - Wash skin after contact with wet lime mixes (alkaline).
          - Do NOT use this material for load-bearing structural elements
            without proper engineering validation.
    """))
    print("\nGuide complete. You now have a full interactive walkthrough for oatmeal-crete v1.0 (mold-resistant, ~4 MPa target).\n")

def main():
    banner()
    batch = choose_batch()
    salt_masses = salt_breakdown(batch["salt_blend"])
    oatmeal_prep_instructions(batch["oatmeal"])
    salt_prep_instructions(salt_masses)
    dry_mix_instructions(batch)
    add_oatmeal_instructions(batch)
    hydration_instructions(batch)
    casting_instructions()
    curing_instructions()
    testing_instructions()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
