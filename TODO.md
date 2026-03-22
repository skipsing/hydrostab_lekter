# TODO: Damage Stability Learning Module

## Goal

Create a learning module (Markdown first, optional LaTeX/PDF export later) covering damage stability with the lost buoyancy method, including theory, worked examples, and exercises.

## Core Topics

- [ ] Barge equilibrium in damage condition with symmetrical filling
- [ ] Reduction in waterplane area and moment of inertia, and resulting reduction in `BM`
- [ ] Barge equilibrium in damage condition with unsymmetrical filling
- [ ] Shift in `LCB` and `LCF`, including longitudinal `BM`
- [ ] Trimming moment due to `BG` arm
- [ ] Distribution of trim
- [ ] Clear bullet-list method for determining `T_A` and `T_F`

## Acceptance Criteria

- [ ] `GM_S > 0 m`
- [ ] `T_S < D`

## Deliverables

- [ ] `docs/en/damage_stability_module.md` (theory + worked examples)
- [ ] `docs/en/damage_stability_exercises.md` (exercise set + solutions)
- [ ] Optional PDF export
- [ ] Optional supporting figures from existing PNG export scenes

## Milestones

### Milestone 1: Skeleton and format decision

- [ ] Select primary format: Markdown
- [ ] Define chapter and section structure
- [ ] Decide where supporting PNGs are needed

Definition of done:
- [ ] Complete document skeleton with headings and placeholders

### Milestone 2: Theory sections

- [ ] Write the theory stepwise (subchapters by concept)
- [ ] Keep notation and symbols consistent across sections
- [ ] Add one short worked example to each main concept

Definition of done:
- [ ] Full method can be followed sequentially from setup to final checks

### Milestone 3: Exercise package

- [ ] Single-concept exercise set
- [ ] Parameter-variation exercise (main particulars, initial draft, compartments)
- [ ] Combined end-to-end exercise
- [ ] Comparison exercise: slack tank free-surface effect vs damaged tank (symmetric centerline case)

Definition of done:
- [ ] Every exercise includes final answer and short solution method

### Milestone 4: Notebook conversion (optional)

- [ ] Convert exercises to Jupyter notebooks
- [ ] Put task text in Markdown cells
- [ ] Add starter code cells with "Your code goes here" prompts
- [ ] Add separate solution notebook

Definition of done:
- [ ] Notebook tasks run and match written exercise answers

### Milestone 5: Review and publish

- [ ] Check equations, units, and symbol definitions
- [ ] Verify acceptance criteria are explicitly evaluated
- [ ] Export final handout format if required

Definition of done:
- [ ] Material is ready for lecture and student self-study






