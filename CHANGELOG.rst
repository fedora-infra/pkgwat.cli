Changelog
=========

0.13
----

- Add support for querying package relationships - Requires `628d840 <https://github.com/fedora-infra/pkgwat.cli/commit/628d840f443216b30181d97dc89d06c2223e89ed>`_
- Merge branch 'release/0.11' into develop `8c93517 <https://github.com/fedora-infra/pkgwat.cli/commit/8c93517f34462b789e62b1ba1327964d00cfaf9f>`_
- Add a guide to using the command help `9426cd3 <https://github.com/fedora-infra/pkgwat.cli/commit/9426cd3ca04d5175ee7cedd1d7421d96166de8d4>`_
- Add a guide to using the command help `49b79fb <https://github.com/fedora-infra/pkgwat.cli/commit/49b79fb16f7cda4c17d6ca43d8601a137ff26408>`_
- Update `128aa79 <https://github.com/fedora-infra/pkgwat.cli/commit/128aa79853c5b6d66ffa5603310b8146d4106582>`_
- Merge pull request #33 from arielb2/develop `68b3bc4 <https://github.com/fedora-infra/pkgwat.cli/commit/68b3bc45f6306cab4a0287219424b453c9581285>`_
- Suggest a method for the description and version `97f8ac9 <https://github.com/fedora-infra/pkgwat.cli/commit/97f8ac9bcd68c30dff1de206e6ad7dea0a8fb0cd>`_
- Merge pull request #36 from arielb2/develop `8110786 <https://github.com/fedora-infra/pkgwat.cli/commit/81107862dbdb504d72dd43fa95bffa2c8525dea1>`_
- Support Command Completions `24f0768 <https://github.com/fedora-infra/pkgwat.cli/commit/24f0768abf0e8baab22bb82a10fa31f3809801e8>`_
- Merge pull request #37 from arielb2/develop `92e3f1f <https://github.com/fedora-infra/pkgwat.cli/commit/92e3f1f906d9dd7415ed37188693eee69050c038>`_
- Remove the arch argument since it not supported in fedora-packages `f30ad13 <https://github.com/fedora-infra/pkgwat.cli/commit/f30ad137131c8a41dde9dd789c2c93df3b639588>`_
- add .cico.pipeline `ae139a4 <https://github.com/fedora-infra/pkgwat.cli/commit/ae139a45b63fc4180e5a655b7333e284255a4c29>`_
- Introduce tox with basic test framework `cb6e938 <https://github.com/fedora-infra/pkgwat.cli/commit/cb6e938042c2235a0f6b6f228bf0bc6d0003b700>`_
- remove custom override of stdout/stderr encoding `68321e4 <https://github.com/fedora-infra/pkgwat.cli/commit/68321e4da6fd7d8d90246e7d21312af877b53333>`_
- tox: bump py36 env to py37 `807a8e8 <https://github.com/fedora-infra/pkgwat.cli/commit/807a8e87773af8d501f0e61f1585c8ce9658ba53>`_
- readme: add instructions how to set up devenv and run tests `e1236a1 <https://github.com/fedora-infra/pkgwat.cli/commit/e1236a1edfd709ba010e32e018c09144e0f799d9>`_
- changelog: remove erroneous extra lines at the bottom `03dc98a <https://github.com/fedora-infra/pkgwat.cli/commit/03dc98a27556b959a703d2c0a09e5dd49a7d1820>`_
- readme: add instructions how to populate changelog `1c9bfb6 <https://github.com/fedora-infra/pkgwat.cli/commit/1c9bfb61114c3c67c1a3473173d3ea1bde329904>`_


0.11
----

- Add short options for pagination.  Fixes #26. `60518720f <https://github.com/fedora-infra/pkgwat.cli/commit/60518720f5f7ddd536a363948c87c29e87a764af>`_
- Merge pull request #27 from fedora-infra/feature/short-options `c8e9d350b <https://github.com/fedora-infra/pkgwat.cli/commit/c8e9d350b9d7d981eb63a40ff8b7cd29347b25d1>`_
- 0.10 `980a4c118 <https://github.com/fedora-infra/pkgwat.cli/commit/980a4c118c1f6b6693e6f0fc543e8e72d99c9fab>`_
- Default to 'info' command if subcommand not found. `3d5ca7626 <https://github.com/fedora-infra/pkgwat.cli/commit/3d5ca7626026377c0ebd72cba3e134e6afa8b1e2>`_
- Merge pull request #28 from fedora-infra/default-info `76a34fa88 <https://github.com/fedora-infra/pkgwat.cli/commit/76a34fa88c8de42e48e4d44172d5437beb43ca0a>`_
- Use da.gd for link shortening. `52be8fd45 <https://github.com/fedora-infra/pkgwat.cli/commit/52be8fd45bcebec9470e2f958fd52d884e9e0dce>`_
- Merge pull request #29 from fedora-infra/feature/dagd `af1bfc02f <https://github.com/fedora-infra/pkgwat.cli/commit/af1bfc02f146d1377c1dcc558bb264f3b20eeead>`_
- Remove these deprecated commands as per fedora-infra/pkgwat.api#22. `0e45b5b9a <https://github.com/fedora-infra/pkgwat.cli/commit/0e45b5b9aedb2edd908a943d029a60e49dd0ae5d>`_
- Merge pull request #31 from fedora-infra/feature/remove-relationships `739aebea1 <https://github.com/fedora-infra/pkgwat.cli/commit/739aebea1a364ffb92bb45eb7f05c5dc7ba103c3>`_
- Remove entry-points from #31. `a5d9e8867 <https://github.com/fedora-infra/pkgwat.cli/commit/a5d9e8867b554555bb1e25c25a50ba64b7cd833d>`_
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1112119 `ac224b6b2 <https://github.com/fedora-infra/pkgwat.cli/commit/ac224b6b2ee46a19cbf5994ae825ea40c4d7cf81>`_

0.9
---

- Show subpackages in search results. `6a19c33fe <https://github.com/fedora-infra/pkgwat.cli/commit/6a19c33fe8eb622a23e79210ee3a3526b49c4a5e>`_
- Merge pull request #19 from fedora-infra/feature/search-subpackages `48d72599a <https://github.com/fedora-infra/pkgwat.cli/commit/48d72599a26cefe30c5f98b89cea609464aaa2e8>`_
- Allow short options. `f27da7004 <https://github.com/fedora-infra/pkgwat.cli/commit/f27da7004d0d46c2b00198aa9cdff9a1b684214c>`_
- "pkgwat history" command. `7a2a7af6d <https://github.com/fedora-infra/pkgwat.cli/commit/7a2a7af6d0cd6abb1d439eaae3c562ab5def6491>`_
- Add support for querying package relationships - Requires `9a558561d <https://github.com/fedora-infra/pkgwat.cli/commit/9a558561df7fe7111fcf20167ce1a64894d52db8>`_
- "pkgwat history" command. `2e85136c7 <https://github.com/fedora-infra/pkgwat.cli/commit/2e85136c74731783b992d072b994267d1839310f>`_
- Remove duplicate entry. `de2ea8832 <https://github.com/fedora-infra/pkgwat.cli/commit/de2ea8832afaac69f0a8145606781291048eb90c>`_
- Protect link formatting. `72446fdc5 <https://github.com/fedora-infra/pkgwat.cli/commit/72446fdc54f978939df6914b5561316650da2147>`_
- Remove dupes. `14a7d71d4 <https://github.com/fedora-infra/pkgwat.cli/commit/14a7d71d43f016e6f14cadb7b8892330b4a7973c>`_
- pkgwat dependants `a880dd888 <https://github.com/fedora-infra/pkgwat.cli/commit/a880dd8882b925734139e0fb9a06536e91e45c0c>`_
- Scrub reference to old repo. `18e09e429 <https://github.com/fedora-infra/pkgwat.cli/commit/18e09e4298b17cf1bb87fd3a1ccae15edf424d5b>`_
- Merge pull request #23 from fedora-infra/feature/url-update `c5fe2af32 <https://github.com/fedora-infra/pkgwat.cli/commit/c5fe2af327916be8b05203380dc6d6d8384dde2f>`_
- Move the version string. `2c7bf9c52 <https://github.com/fedora-infra/pkgwat.cli/commit/2c7bf9c52eb9bc105101ea5afc9f2c07bca61a95>`_

0.8
---

- Add support for querying package relationships - Requires `e082db430 <https://github.com/fedora-infra/pkgwat.cli/commit/e082db430a6739800824ddf8c95e166a09cec39a>`_
- "pkgwat history" command. `60a2e42a0 <https://github.com/fedora-infra/pkgwat.cli/commit/60a2e42a0d915e4c83b0f790c86dd4b84c07a93c>`_
- Remove section from "search" that is only applicable to "info" `997f61de4 <https://github.com/fedora-infra/pkgwat.cli/commit/997f61de48c9a066027efb2abfe881a40ed5e9cb>`_
- 0.8 `7e403f79f <https://github.com/fedora-infra/pkgwat.cli/commit/7e403f79fb2e05181b61fbcc647a190104c343f0>`_

0.7
---

- "pkgwat history" command. `cb315f8fa <https://github.com/fedora-infra/pkgwat.cli/commit/cb315f8facab336f9fa5e755ff9768574102cde6>`_
- Merge pull request #15 from fedora-infra/feature/history `8b8d7ca35 <https://github.com/fedora-infra/pkgwat.cli/commit/8b8d7ca3573562e74f7b0f4aab7ab3953dae435e>`_
- No shows information subpackages. `8f5a84cc2 <https://github.com/fedora-infra/pkgwat.cli/commit/8f5a84cc2dbac133c326aefceb5a7caada819c79>`_
- Merge pull request #14 from arielb2/develop `8d24de395 <https://github.com/fedora-infra/pkgwat.cli/commit/8d24de395ecd2d3256b3286352b8254678cdd29c>`_

0.6
---

- Be more careful with data coming back from /packages. `a7f022f15 <https://github.com/fedora-infra/pkgwat.cli/commit/a7f022f1572643e4d9644ca8e89b669aa6df5a9a>`_
- Disable that annoying message.  Fixes #9. `18d4363c7 <https://github.com/fedora-infra/pkgwat.cli/commit/18d4363c7f0cf332714333aa2234ace43f0200b7>`_
- Depend on Pillow, instead of PIL. `e0c4d7d4d <https://github.com/fedora-infra/pkgwat.cli/commit/e0c4d7d4dcb25404033382fe123c1be58b4ebcb2>`_
- Merge pull request #11 from fedora-infra/hotfix/pillow-not-pil `f0da8304b <https://github.com/fedora-infra/pkgwat.cli/commit/f0da8304b12d46ee8348d9d2367d1533c9077cd0>`_

0.5
---

- Protect against unicode madness in file redirection. `c1ddc0984 <https://github.com/fedora-infra/pkgwat.cli/commit/c1ddc09846e423e5b448fbe3441ef7ccb967fbf3>`_
- Use full update title, not just id. `a3edd9534 <https://github.com/fedora-infra/pkgwat.cli/commit/a3edd9534b018ae10d92cc8a99c0036737c5594d>`_
