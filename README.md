# Web Engineering Skills

This workspace develops one portable Agent Skill for web architecture and implementation. Start with the [skill entry point](web-engineering/SKILL.md) or the [Phase 1 report](docs/PHASE_1.md).

Run `python3 scripts/validate.py` to check skill metadata, rules and local links. With TypeScript and Node available, compile the neutral examples into a temporary directory and run their executable assertions:

```sh
example_out="$(mktemp -d)"
tsc --strict --target ES2022 --module NodeNext --moduleResolution NodeNext \
  --outDir "$example_out" web-engineering/assets/examples/*.ts
node scripts/validate_examples.cjs "$example_out"
```

The [coverage audit](docs/PHASE_1_COVERAGE_AUDIT.md) records the final React domain and portability assessment. To rerun the optional React DOM smoke after compiling the examples, install React and React DOM 19.2.4 and jsdom 26.1.0 into a temporary prefix. Run `NODE_PATH=<prefix>/node_modules node scripts/smoke_react.cjs "$example_out"`.

The [Phase 2 extraction](docs/PHASE_2.md) and [integration report](docs/PHASE_2_INTEGRATION.md) document the unified React and Next.js skill. See the [roadmap](ROADMAP.md) for phase status.

The [Phase 3 integration](docs/PHASE_3_INTEGRATION.md) includes a conditional Supabase backend profile and isolated validation results.

See the [consolidation report](docs/PHASE_4.md) and [packaging guidance](docs/SKILL_ARCHITECTURE.md). The standalone skill directory is `web-engineering/`.
