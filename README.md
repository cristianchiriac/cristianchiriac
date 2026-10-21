<div align="center">

<sub>DEFENSIVE SECURITY  /  DETECTION ENGINEERING  /  OPEN SOURCE</sub>

# Cristian Chiriac

### Making security telemetry actionable.

I investigate attacker behavior, build detections, and improve the tools that help defenders make better decisions.

**Cybersecurity Engineer** · Threat Hunting · DFIR · Security Engineering

[**Selected work ↓**](#selected-upstream-work) &nbsp;·&nbsp; [**Merged contributions ↓**](#open-source-contributions) &nbsp;·&nbsp; [**ORCID ↗**](https://orcid.org/0009-0006-0583-046X)

</div>

---

## What I work on

| **01 / Detection** | **02 / Investigation** | **03 / Engineering** |
|:--|:--|:--|
| Detection logic, Sigma rules, telemetry quality and ATT&CK mapping. | Threat hunting, endpoint evidence, incident investigation and forensic workflows. | Reliable security tooling, tests, safer defaults and maintainable automation. |

I care about the distance between **an event being collected** and **an analyst being able to act on it**. Most of my work sits in that gap.

## Selected upstream work

A few shipped fixes that illustrate the kinds of problems I work on. Each link goes to the actual accepted pull request.

| Focus | Contribution and why it matters |
|:--|:--|
| **Detection fidelity** | [pySigma #585](https://github.com/SigmaHQ/pySigma/pull/585) — respect the rule's regex policy instead of silently forcing RE2. |
| **Query correctness** | [Splunk Sigma backend #77](https://github.com/SigmaHQ/pySigma-backend-splunk/pull/77) — correct Boolean precedence that could broaden generated SPL/SPL2 searches. |
| **Threat-hunting coverage** | [Sysmon Modular #227](https://github.com/olafhartong/sysmon-modular/pull/227) — correctly map WMI permanent subscriptions to MITRE ATT&CK T1546.003. |
| **Forensic tooling** | [Volatility 3 #2035](https://github.com/volatilityfoundation/volatility3/pull/2035) — replace misleading Windows plugin crashes with actionable errors. |
| **Security control lifecycle** | [Firewalla #9954](https://github.com/firewalla/firewalla/pull/9954) — ensure domain rules with IP TTL settings are properly removed. |
| **Operational reliability** | [Yeti #1408](https://github.com/yeti-platform/yeti/pull/1408) — fix dependency installation that prevented scheduled feed tests from running. |
| **Endpoint workflow** | [Velociraptor #5086](https://github.com/Velocidex/velociraptor/pull/5086) — repair the VQL shell's Repeat action. |

<sub>Also contributing across [Firewalla](https://github.com/firewalla/firewalla), [DefectDojo](https://github.com/DefectDojo/django-DefectDojo), [Nuxt UI](https://github.com/nuxt/ui), [pySigma](https://github.com/SigmaHQ/pySigma), and other maintained upstream projects.</sub>

## Open source contributions

<!-- BEGIN AUTO-GENERATED CONTRIBUTIONS -->
**95 accepted pull requests** across **72 independent upstream repositories**.

Every PR below is merged into the upstream project, not merely submitted from a fork.

<details>
<summary><strong>Explore the complete contribution log</strong> — 95 merged PRs / 72 repositories</summary>

| Upstream | Latest merged change | Accepted PRs |
|:--|:--|:--|
| [firewalla/firewalla](https://github.com/firewalla/firewalla) | Keep the ipv4 entries of hostsdb in sync on Host:Updated | [#9959](https://github.com/firewalla/firewalla/pull/9959) · [#9954](https://github.com/firewalla/firewalla/pull/9954) · [#9953](https://github.com/firewalla/firewalla/pull/9953) · [#9910](https://github.com/firewalla/firewalla/pull/9910) · [#9909](https://github.com/firewalla/firewalla/pull/9909) |
| [SigmaHQ/pySigma](https://github.com/SigmaHQ/pySigma) | fix: compile \|re values with the rule's policy | [#585](https://github.com/SigmaHQ/pySigma/pull/585) · [#545](https://github.com/SigmaHQ/pySigma/pull/545) · [#544](https://github.com/SigmaHQ/pySigma/pull/544) · [#542](https://github.com/SigmaHQ/pySigma/pull/542) · [#541](https://github.com/SigmaHQ/pySigma/pull/541) |
| [caronc/apprise](https://github.com/caronc/apprise) | Keep cc/bcc/reply display names intact in email url() | [#1812](https://github.com/caronc/apprise/pull/1812) · [#1813](https://github.com/caronc/apprise/pull/1813) · [#1807](https://github.com/caronc/apprise/pull/1807) · [#1808](https://github.com/caronc/apprise/pull/1808) |
| [ComplianceAsCode/content](https://github.com/ComplianceAsCode/content) | al2023: map CIS 4.3.4 to sudo_remove_no_authenticate | [#15167](https://github.com/ComplianceAsCode/content/pull/15167) · [#15165](https://github.com/ComplianceAsCode/content/pull/15165) · [#15164](https://github.com/ComplianceAsCode/content/pull/15164) |
| [posit-dev/pointblank](https://github.com/posit-dev/pointblank) | fix: explain why col_summary_tbl() fails when no column can be profiled | [#469](https://github.com/posit-dev/pointblank/pull/469) · [#444](https://github.com/posit-dev/pointblank/pull/444) · [#445](https://github.com/posit-dev/pointblank/pull/445) |
| [Velocidex/velociraptor](https://github.com/Velocidex/velociraptor) | Fix the repeat button in the VQL shell | [#5086](https://github.com/Velocidex/velociraptor/pull/5086) · [#5047](https://github.com/Velocidex/velociraptor/pull/5047) · [#5016](https://github.com/Velocidex/velociraptor/pull/5016) |
| [henriquesebastiao/downtify](https://github.com/henriquesebastiao/downtify) | Match titles with a dash against candidates with a feat. suffix | [#435](https://github.com/henriquesebastiao/downtify/pull/435) · [#434](https://github.com/henriquesebastiao/downtify/pull/434) |
| [strictdoc-project/strictdoc](https://github.com/strictdoc-project/strictdoc) | fix(backend/reqif): import Parent relations between different node types | [#3243](https://github.com/strictdoc-project/strictdoc/pull/3243) · [#3244](https://github.com/strictdoc-project/strictdoc/pull/3244) |
| [ydkhatri/mac_apt](https://github.com/ydkhatri/mac_apt) | Declare the BIOME Data column as text | [#175](https://github.com/ydkhatri/mac_apt/pull/175) · [#176](https://github.com/ydkhatri/mac_apt/pull/176) |
| [coin-or/pulp](https://github.com/coin-or/pulp) | Keep binary bounds in nested add_variable_dicts and add_variable_matrix | [#964](https://github.com/coin-or/pulp/pull/964) · [#953](https://github.com/coin-or/pulp/pull/953) |
| [Flexget/Flexget](https://github.com/Flexget/Flexget) | Apply the session's max_retries to https:// requests | [#5264](https://github.com/Flexget/Flexget/pull/5264) · [#5263](https://github.com/Flexget/Flexget/pull/5263) |
| [dgunning/edgartools](https://github.com/dgunning/edgartools) | fix(search): drop an amendment form code whose root form is also listed | [#1545](https://github.com/dgunning/edgartools/pull/1545) · [#1533](https://github.com/dgunning/edgartools/pull/1533) |
| [python/typeshed](https://github.com/python/typeshed) | [networkx] Accept any node type in graph functions that took Graph[Hashable] | [#16557](https://github.com/python/typeshed/pull/16557) |
| [SumoLogic/pySigma-backend-sumologic](https://github.com/SumoLogic/pySigma-backend-sumologic) | Fix cse_rule output format | [#16](https://github.com/SumoLogic/pySigma-backend-sumologic/pull/16) |
| [ipython/ipython](https://github.com/ipython/ipython) | Install ipykernel test requirements from its dependency group in downstream CI | [#15418](https://github.com/ipython/ipython/pull/15418) |
| [typstyle-rs/typstyle](https://github.com/typstyle-rs/typstyle) | fix: parse enum marker numbers as u64 | [#520](https://github.com/typstyle-rs/typstyle/pull/520) |
| [arviz-devs/arviz-stats](https://github.com/arviz-devs/arviz-stats) | Reduce MAD over sample_dims in summary median kinds | [#496](https://github.com/arviz-devs/arviz-stats/pull/496) |
| [mui/base-ui](https://github.com/mui/base-ui) | [popover] Keep focus that moved elsewhere before the deferred focus restore | [#6015](https://github.com/mui/base-ui/pull/6015) |
| [komari-monitor/komari](https://github.com/komari-monitor/komari) | fix(metricstore): give the ping queue its own capacity | [#695](https://github.com/komari-monitor/komari/pull/695) |
| [fedora-infra/anitya](https://github.com/fedora-infra/anitya) | Use re.error instead of sre_constants.error (Python 3.15) | [#2130](https://github.com/fedora-infra/anitya/pull/2130) |
| [quasarframework/quasar](https://github.com/quasarframework/quasar) | fix(ui): compare the hash route path when releasing the iOS scroll lock #18573 | [#18574](https://github.com/quasarframework/quasar/pull/18574) |
| [falcosecurity/falco](https://github.com/falcosecurity/falco) | fix(userspace/falco): recover file_output from a failed write | [#4036](https://github.com/falcosecurity/falco/pull/4036) |
| [yukinarit/pyserde](https://github.com/yukinarit/pyserde) | Support Python 3.15: use dataclasses.MISSING instead of _MISSING_TYPE | [#812](https://github.com/yukinarit/pyserde/pull/812) |
| [BottlecapDave/HomeAssistant-OctopusEnergy](https://github.com/BottlecapDave/HomeAssistant-OctopusEnergy) | fix: Default "favour direct debit rates" to on when adding an account | [#1918](https://github.com/BottlecapDave/HomeAssistant-OctopusEnergy/pull/1918) |
| [Koenkk/zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt) | fix: Look up the endpoint name of a group member to check its state | [#33410](https://github.com/Koenkk/zigbee2mqtt/pull/33410) |
| [eugenioenko/ttt](https://github.com/eugenioenko/ttt) | fix(search): clear find highlights when closing find on a content tab | [#950](https://github.com/eugenioenko/ttt/pull/950) |
| [getsentry/spotlight](https://github.com/getsentry/spotlight) | fix(dev): Run the sidecar with --experimental-strip-types for Node 26 | [#1364](https://github.com/getsentry/spotlight/pull/1364) |
| [Hexagon/croner](https://github.com/Hexagon/croner) | Fix previousRuns() for months shorter than 31 days | [#409](https://github.com/Hexagon/croner/pull/409) |
| [yomidevs/yomitan](https://github.com/yomidevs/yomitan) | Add CJK Unified Ideographs Extension J to the CJK ranges | [#2504](https://github.com/yomidevs/yomitan/pull/2504) |
| [marcosschroh/dataclasses-avroschema](https://github.com/marcosschroh/dataclasses-avroschema) | fix: compare union defaults with dataclasses.MISSING (Python 3.15) | [#984](https://github.com/marcosschroh/dataclasses-avroschema/pull/984) |
| [florianfesti/boxes](https://github.com/florianfesti/boxes) | TrayLayout: accept the escaped layout from the SVG command line | [#977](https://github.com/florianfesti/boxes/pull/977) |
| [callowayproject/bump-my-version](https://github.com/callowayproject/bump-my-version) | Keep the repository root when HEAD is detached | [#439](https://github.com/callowayproject/bump-my-version/pull/439) |
| [eternnoir/pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) | Treat RichText strings as JSON only when they parse to an object | [#2635](https://github.com/eternnoir/pyTelegramBotAPI/pull/2635) |
| [kucherenko/jscpd](https://github.com/kucherenko/jscpd) | fix(semantic): count a JSX element of a component as a call | [#1211](https://github.com/kucherenko/jscpd/pull/1211) |
| [atuinsh/atuin](https://github.com/atuinsh/atuin) | fix(config): let ATUIN_* environment variables override config.toml | [#4438](https://github.com/atuinsh/atuin/pull/4438) |
| [HKUDS/nanobot](https://github.com/HKUDS/nanobot) | fix(cli): set SPT_NOENV only on Linux | [#6232](https://github.com/HKUDS/nanobot/pull/6232) |
| [lingui/swc-plugin](https://github.com/lingui/swc-plugin) | fix: transform a useLingui `t` nested in a placeholder of another `t` | [#285](https://github.com/lingui/swc-plugin/pull/285) |
| [OHF-Voice/wyoming-faster-whisper](https://github.com/OHF-Voice/wyoming-faster-whisper) | Constrain PyAV below 19 until faster-whisper supports it | [#130](https://github.com/OHF-Voice/wyoming-faster-whisper/pull/130) |
| [unitaryai/detoxify](https://github.com/unitaryai/detoxify) | Drop pytest-flake8 from test requirements to fix CI on pytest 9 | [#137](https://github.com/unitaryai/detoxify/pull/137) |
| [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular) | Map WMI event subscription events (EID 19/20/21) to T1546.003 | [#227](https://github.com/olafhartong/sysmon-modular/pull/227) |
| [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis) | fix(speech): constrain PyAV below 19 for faster-whisper | [#1094](https://github.com/open-jarvis/OpenJarvis/pull/1094) |
| [JFryy/qq](https://github.com/JFryy/qq) | Stringify non-string YAML mapping keys (fixes #73) | [#74](https://github.com/JFryy/qq/pull/74) |
| [pyxem/orix](https://github.com/pyxem/orix) | Support Matplotlib 3.12 ArtistList location | [#688](https://github.com/pyxem/orix/pull/688) |
| [Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube) | Constrain PyAV when installing whisper-ctranslate2 | [#7815](https://github.com/Chocobozzz/PeerTube/pull/7815) |
| [orval-labs/orval](https://github.com/orval-labs/orval) | fix(core): do not alias self-referencing schemas in single schemas mode | [#4298](https://github.com/orval-labs/orval/pull/4298) |
| [nuxt/ui](https://github.com/nuxt/ui) | perf(useComponentProps): skip prop resolution for Vue internal flags | [#7186](https://github.com/nuxt/ui/pull/7186) |
| [boa-dev/boa](https://github.com/boa-dev/boa) | fix(engine): accept lone surrogate escapes in JSON.parse | [#5578](https://github.com/boa-dev/boa/pull/5578) |
| [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech) | Add an opt-in --torch_num_threads setting for PyTorch CPU threads | [#707](https://github.com/huggingface/speech-to-speech/pull/707) |
| [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | fix(batch): give node a Windows path for PROJECT_DIR under Git Bash | [#5051](https://github.com/career-ops-hq/career-ops/pull/5051) |
| [Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth) | fonts: find CJK fonts on Windows, allow a GEO_FONT override | [#13](https://github.com/Oldcircle/geo-sleuth/pull/13) |
| [volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3) | Windows: Raise TypeError instead of a bare raise in virtmap and crashinfo | [#2035](https://github.com/volatilityfoundation/volatility3/pull/2035) |
| [NetroScript/Graveyard-Keeper-Savefile-Editor](https://github.com/NetroScript/Graveyard-Keeper-Savefile-Editor) | Read the Eel version with importlib.metadata (fixes #106) | [#107](https://github.com/NetroScript/Graveyard-Keeper-Savefile-Editor/pull/107) |
| [sgl-project/sglang-omni](https://github.com/sgl-project/sglang-omni) | [ASR] Probe audio duration with PyAV 19 | [#2557](https://github.com/sgl-project/sglang-omni/pull/2557) |
| [bacescuandrei/macos-inspector](https://github.com/bacescuandrei/macos-inspector) | Remove unused imports and variables | [#1](https://github.com/bacescuandrei/macos-inspector/pull/1) |
| [oreilles/polars-st](https://github.com/oreilles/polars-st) | Fix import on Polars 2 (GeoSeries metaclass conflict) | [#85](https://github.com/oreilles/polars-st/pull/85) |
| [datajuicer/data-juicer](https://github.com/datajuicer/data-juicer) | fix(mapper): use the Lexbor parser in clean_html_mapper | [#1085](https://github.com/datajuicer/data-juicer/pull/1085) |
| [Kometa-Team/Quickstart](https://github.com/Kometa-Team/Quickstart) | Skip no-commit-to-branch in the Lint workflow | [#1878](https://github.com/Kometa-Team/Quickstart/pull/1878) |
| [turbot/steampipe-mod-aws-compliance](https://github.com/turbot/steampipe-mod-aws-compliance) | Fix port ranges in vpc_security_group_restricted_common_ports query | [#978](https://github.com/turbot/steampipe-mod-aws-compliance/pull/978) |
| [arxhr007/Aliens_eye](https://github.com/arxhr007/Aliens_eye) | Use the Lexbor parser of selectolax (fix ImportError with selectolax 1.0) | [#23](https://github.com/arxhr007/Aliens_eye/pull/23) |
| [yeti-platform/yeti](https://github.com/yeti-platform/yeti) | Install the plugins dependency group in the feed tests workflow | [#1408](https://github.com/yeti-platform/yeti/pull/1408) |
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | Constrain PyAV below 19 in requirements.txt | [#1582](https://github.com/harry0703/MoneyPrinterTurbo/pull/1582) |
| [Kometa-Team/Kometa](https://github.com/Kometa-Team/Kometa) | Report failed Apprise notifications with Apprise 2 | [#3690](https://github.com/Kometa-Team/Kometa/pull/3690) |
| [wayne-csrs/pySigma-backend-signals](https://github.com/wayne-csrs/pySigma-backend-signals) | fix: keep correlation event_type unquoted with pySigma &gt;= 1.5.1 | [#9](https://github.com/wayne-csrs/pySigma-backend-signals/pull/9) |
| [kaixxx/noScribe](https://github.com/kaixxx/noScribe) | Pin PyAV below 19 until faster-whisper supports it | [#367](https://github.com/kaixxx/noScribe/pull/367) |
| [ipython/ipykernel](https://github.com/ipython/ipykernel) | Update README install command for the test dependency group | [#1573](https://github.com/ipython/ipykernel/pull/1573) |
| [Softcatala/whisper-ctranslate2](https://github.com/Softcatala/whisper-ctranslate2) | Constrain PyAV below 19 in the package requirements | [#154](https://github.com/Softcatala/whisper-ctranslate2/pull/154) |
| [nornir-automation/nornir](https://github.com/nornir-automation/nornir) | Deprecate legacy Jinja2 rendering helpers | [#1103](https://github.com/nornir-automation/nornir/pull/1103) |
| [logpoint/pySigma-backend-logpoint](https://github.com/logpoint/pySigma-backend-logpoint) | Fix AttributeError for numeric pipeline pre-filter values | [#38](https://github.com/logpoint/pySigma-backend-logpoint/pull/38) |
| [DefectDojo/django-DefectDojo](https://github.com/DefectDojo/django-DefectDojo) | fix(govulncheck): don't crash on OSV entries without aliases | [#16014](https://github.com/DefectDojo/django-DefectDojo/pull/16014) |
| [SigmaHQ/pySigma-backend-crowdstrike](https://github.com/SigmaHQ/pySigma-backend-crowdstrike) | fix: OR nested inside AND was not parenthesized, widening the emitted query | [#25](https://github.com/SigmaHQ/pySigma-backend-crowdstrike/pull/25) |
| [SigmaHQ/pySigma-backend-splunk](https://github.com/SigmaHQ/pySigma-backend-splunk) | fix: OR/AND precedence inversion widens emitted queries in SPL and SPL2 backends | [#77](https://github.com/SigmaHQ/pySigma-backend-splunk/pull/77) |
| [benmoran56/esper](https://github.com/benmoran56/esper) | Fix _get_components() dropping a filter type when the min-size set changes twice | [#124](https://github.com/benmoran56/esper/pull/124) |

</details>

<sub>Maintained automatically from verified GitHub merges. Latest: 2026-10-20 (UTC). Open and closed-unmerged PRs are excluded.</sub>

[**View the complete upstream history ↗**](https://github.com/search?q=author%3Acristianchiriac+is%3Apr+is%3Amerged&type=pullrequests)
<!-- END AUTO-GENERATED CONTRIBUTIONS -->

---

## Independent work

**[Yahoo IMAP Scanner / Local Mail Guardian ↗](https://github.com/cristianchiriac/Yahoo-IMAP-Spam-Cleaner)**

A local-first phishing and spam analysis tool with explainable detection signals, a CLI and local web interface. Built around read-only scanning by default, explicit approval for mailbox changes, and privacy-conscious reporting.

## My engineering approach

- **Reproduce before patching.** Start with the observed failure, then write a focused test that would fail without the fix.
- **Prefer precise changes.** Small patches are useful when they resolve a real failure; complexity is not a measure of impact.
- **Preserve security boundaries.** Favor understandable defaults, testable behavior, and clear failure handling.
- **Leave evidence.** Link issues, tests, review discussions, and upstream acceptance rather than relying on self-reported metrics.

---

<div align="center">

**Defensive security, grounded in evidence.**

[GitHub activity](https://github.com/cristianchiriac?tab=overview) &nbsp;·&nbsp; [All merged PRs](https://github.com/search?q=author%3Acristianchiriac+is%3Apr+is%3Amerged&type=pullrequests) &nbsp;·&nbsp; [ORCID](https://orcid.org/0009-0006-0583-046X)

</div>
