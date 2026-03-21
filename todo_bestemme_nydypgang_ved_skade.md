
# TODO: Bestemme Nydypgang Ved Skade

## Goal

Create a teaching document (Markdown first, optional LaTeX export later) that explains how to determine new equilibrium in damage condition with parallel submergence using the lost buoyancy method.

The content must follow the same phase order as the current `barge_*` damage scene sequence.

## Scope

- In scope:
	- Sequential method description
	- Short worked examples for each phase
	- One complete end-to-end example
	- Exercises with final answers
- Out of scope (for this TODO):
	- New Manim scene development
	- UI/website packaging

## Deliverables

- [ ] `damage_equilibrium_module.md` with full theory and worked examples
- [ ] `damage_equilibrium_exercises.md` with exercises and solutions
- [ ] Optional PDF export from Markdown (Pandoc/Quarto)

## Recommended Chapter Order (aligned with scenes)

- [ ] 1. Geometry and baseline hydrostatics recap
- [ ] 2. Damage case setup and symmetric flooding assumptions
- [ ] 3. Parallel submergence and new displaced volume
- [ ] 4. Updated hydrostatics after damage (`KB`, `BM`, `GM`)
- [ ] 5. Longitudinal effects for unsymmetric damage (`LCB`, `LCF`, longitudinal `BM`)
- [ ] 6. Trimming moment, trim distribution, and determination of `T_A` and `T_F`
- [ ] 7. Final acceptance checks (`GM_S > 0`, `T_S < D`)

## Milestones

### Milestone 1: Skeleton and notation

- [ ] Decide primary format: Markdown
- [ ] Add symbol table, units, and sign conventions
- [ ] Add chapter skeleton with placeholders

Definition of done:
- [ ] Document structure is complete and ready for content writing

### Milestone 2: Theory blocks by phase

- [ ] Write each phase as step-by-step procedure
- [ ] Keep equations and variable names consistent with scene labels
- [ ] Add assumptions and validity limits per phase

Definition of done:
- [ ] A reader can follow the full method without external references

### Milestone 3: Worked examples

- [ ] Add one short numeric example per phase
- [ ] Add one full-chain example from damage to final drafts
- [ ] Include intermediate values for checking

Definition of done:
- [ ] All example calculations can be reproduced from given data

### Milestone 4: Exercises

- [ ] Drill exercises (single concept at a time)
- [ ] Parameter-variation exercise (main particulars, draft, compartments)
- [ ] Combined full-method exercise
- [ ] Comparison exercise: slack tank FSE vs damaged flooded tank (symmetric case)

Definition of done:
- [ ] Each exercise has final answer and short solution outline

### Milestone 5: QA and publishing

- [ ] Technical review of notation, units, and equation consistency
- [ ] Cross-check chapter order against scene sequence
- [ ] Export to PDF if needed

Definition of done:
- [ ] Document is classroom-ready

## Acceptance Criteria

- [ ] Method is fully sequential and mirrors scene order
- [ ] Equations are dimensionally consistent and symbols are defined
- [ ] The student can compute new equilibrium drafts for at least one complete case
- [ ] Acceptance checks are explicit: `GM_S > 0 m` and `T_S < D`

## Optional Next Step (Notebooks)

- [ ] Convert exercises to Jupyter notebooks
- [ ] Task text in Markdown cells, starter templates in code cells
- [ ] Provide separate solution notebook

