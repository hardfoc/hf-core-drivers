# Updating submodules

Move a driver to a newer commit, check it and open the pull request that pins it.

<div class="hf-steps" markdown>

1. **Merge the change in the driver's repository first.** The umbrella only ever points at commits on a driver's
   `main`.
2. **Bump the pointer here.**

    ```bash
    git switch -c bump/hf-tmc9660-driver
    git submodule update --init external/hf-tmc9660-driver
    git -C external/hf-tmc9660-driver fetch origin main
    git -C external/hf-tmc9660-driver checkout origin/main
    git add external/hf-tmc9660-driver
    git commit -m "Bump hf-tmc9660-driver for <the change>"
    ```

3. **Build it where it is used.** Point hf-core's `hf-core-drivers` submodule at your branch and run its host build
   and the ESP32 examples of the boards that enable the driver.
4. **Open the pull request** here, naming the driver change it brings in. After the merge, bump
   `hf-core-drivers` in hf-core.

</div>

## Adding a driver

1. `git submodule add https://github.com/hardfoc/<repo>.git external/<repo>`.
2. Add an entry for it to [`tools/docs/drivers.yml`](../tools/docs/drivers.yml): group, chip, vendor, function,
   bus, language and whether it has a documentation site. Check each fact against the driver's README.
3. Run `hardfoc-docs gen` and `mkdocs build --strict`; the catalogue gains a card.

## Checking where every submodule points

```bash
git submodule status            # commit of each submodule; a leading '-' means not initialised
git submodule foreach --quiet 'echo "$name $(git describe --tags --always)"'
```

Next: [Coding standards](coding-standards.md).
