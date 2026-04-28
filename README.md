## Setup

1. Get the benchmarks (the following command clones the [sv-benchmarks](https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks)
   repository or updates it if it is already present):
```bash
./scripts/update_benchmarks.sh
```
2. Install [infer](https://github.com/facebook/infer). If it is not available in $PATH, set an absolute path to it in `config.env`.
2. Install [benchexec](https://github.com/sosy-lab/benchexec/blob/main/doc/INSTALL.md#debianubuntu).
3. Install Infer's tool-info modules for benchexec:
```sh
pip install -e analysers/
```

## Running

Use the following command:
```sh
benchexec -N 8 benchmark-defs/infer-heap_and_linked_lists.xml --tool-directory=analysers/bin/infer-wrapper/
```
