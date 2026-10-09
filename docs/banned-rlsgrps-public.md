# Banned Release Groups

This page lists release groups (RlsGrps) that TRaSH-Guides flags, based on community reports, our own testing, and the LQ, LQ (Release Title), and Generated Dynamic HDR custom formats for Radarr and Sonarr. Where available, the PR column links to the merged, closed pull request that added the group. The tabs below the table show which Custom Format each group is in.

| RlsGrp | Reason | PR |
| --- | --- | --- |
| 126811 | Hit-or-miss on including the release group name, which can disrupt automation due to poor naming; non-retail audio; Generated Dynamic HDR; Hybrids without grade checks. | [#2895](https://github.com/TRaSH-Guides/Guides/pull/2895) |
| 1XBET | Releases contain adverts and watermarks. | [#1679](https://github.com/TRaSH-Guides/Guides/pull/1679) |
| 24xHD | They don't include the used codec in the file or release name. | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
| 41RGB | Uses the wrong audio formats in the release name. | [#1533](https://github.com/TRaSH-Guides/Guides/pull/1533) |
| 4K4U | Quality. | [#333](https://github.com/TRaSH-Guides/Guides/pull/333) |
| AOC | Releases are TS/CAM rips that are badly named, leading to incorrect ranking; Pre-retail releases | [#2396](https://github.com/TRaSH-Guides/Guides/pull/2396) |
| AROMA | ALL Re-Tagging | [#333](https://github.com/TRaSH-Guides/Guides/pull/333) |
| aXXo | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| AZAZE | 4K Dolby Vision IMAX Blu-ray encodes that do not include an HDR10 fallback. | [#1162](https://github.com/TRaSH-Guides/Guides/pull/1162) |
| BARC0DE | Not documented | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#468](https://github.com/TRaSH-Guides/Guides/pull/468) re-added |
| BAUCKLEY | Bad audio, gore scenes are cut, and odd alcohol warnings appear throughout the movie. The audio track is also sometimes mislabeled as Hindi for no clear reason. | [#2168](https://github.com/TRaSH-Guides/Guides/pull/2168) |
| BdC | Not documented | [#640](https://github.com/TRaSH-Guides/Guides/pull/640) |
| beAst | Not documented | `ede09001` (direct commit) |
| BEN THE MEN | Releases are badly named and do not include the quality (WEB, Blu-ray, and so on), which breaks automation; low quality. | [#1773](https://github.com/TRaSH-Guides/Guides/pull/1773) |
| BiTOR (2160p) | Generated Dynamic HDR; ENCODEs; non-retail audio; 2160p releases added to LQ (Release Title); 1080p releases are untiered rather than banned. | Radarr LQ: [#1048](https://github.com/TRaSH-Guides/Guides/pull/1048) added → [#1607](https://github.com/TRaSH-Guides/Guides/pull/1607) removed<br>Radarr LQ (Release Title): [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ (Release Title): [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ (Release Title) |
| BRiNK | Not documented | Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| BTM | Release titles do not format the release group name properly or include the quality (for example Blu-ray or WEB-DL), which breaks automation. | [#2377](https://github.com/TRaSH-Guides/Guides/pull/2377) |
| C1NEM4 | CAM releases labeled as WEB-DL, filled with advertisements, including floating text, clips between scenes, and large graphics. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
| C4K | Not documented | [#333](https://github.com/TRaSH-Guides/Guides/pull/333) |
| CDDHD | Not documented | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#468](https://github.com/TRaSH-Guides/Guides/pull/468) re-added |
| CHAOS | Not documented | [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
| CHD | Not documented | Radarr LQ: `ede09001` (direct commit) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
| CHX | Not documented | Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| CiNE | Fake releases: labeled as the new Spider-Man (Across the Spider-Verse) but actually the old movie. | [#1352](https://github.com/TRaSH-Guides/Guides/pull/1352) |
| CLEANUP | Low-quality group, similar to SyncUP (name-dropped in SyncUP release notes as an affiliated low-quality group). | [#2801](https://github.com/TRaSH-Guides/Guides/pull/2801) |
| COLLECTiVE | CAM releases labeled as WEB-DL. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
| CREATiVE24 | Quality | [#1068](https://github.com/TRaSH-Guides/Guides/pull/1068), [#2274](https://github.com/TRaSH-Guides/Guides/pull/2274) |
| CrEwSaDe | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| CTFOH | 4K/HDR releases where no HDR release is available; Quality | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
| d3g | Microsized releases; All Low quality \| Hardware encodes | [#333](https://github.com/TRaSH-Guides/Guides/pull/333), [#1562](https://github.com/TRaSH-Guides/Guides/pull/1562) |
| D3US | Release names do not follow naming conventions, so they cannot be reliably parsed. | [#2439](https://github.com/TRaSH-Guides/Guides/pull/2439) |
| DDR | Renames UHDClub's releases. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| DepraveD | Generated Dynamic HDR; also added to Sonarr LQ, as some TV releases were identified too. | Radarr LQ: [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ: [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
| DNL | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| DRX | Uses non-retail audio; Quality | [#2466](https://github.com/TRaSH-Guides/Guides/pull/2466) |
| E | User-generated Atmos, poorly named files, upmixed audio. | [#2436](https://github.com/TRaSH-Guides/Guides/pull/2436) |
| EPiC | Wrong audio format listed in the release name. | [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
| EuReKA | Not documented | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#468](https://github.com/TRaSH-Guides/Guides/pull/468) re-added |
| EVO (no WEBDL) | Encode, Quality; encodes: BluRay & WEBRip (WEB-DL are okay); WEBs / ENCODEs; Encode Quality; WEB-DLs are allowed | Radarr LQ: [#640](https://github.com/TRaSH-Guides/Guides/pull/640) added → [#664](https://github.com/TRaSH-Guides/Guides/pull/664) removed (EVO moves to its own EVO (no WEBDL) CF)<br>Radarr LQ (Release Title): [#2386](https://github.com/TRaSH-Guides/Guides/pull/2386) moved from the EVO (no WEBDL) CF |
| EVO | Often banned for low-quality Blu-ray releases (EVO (no WEBDL) description in the Radarr guide). | [#610](https://github.com/TRaSH-Guides/Guides/pull/610) |
| FaNGDiNG0 | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| Feranki1980 | Low-quality, microsized releases. | [#2320](https://github.com/TRaSH-Guides/Guides/pull/2320) |
| FGT | Bloated with unnecessary audio tracks, re-tagging; ALL Re-Tagging; unless no other encode is available; All Low Quality \| Bloated Releases; (Movie WEB-DLs allowed)- Sister group of RARBG. Same ethics and practices. | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added<br>Sonarr LQ: [#1007](https://github.com/TRaSH-Guides/Guides/pull/1007) added |
| Flights | Generated Dynamic HDR | [#2429](https://github.com/TRaSH-Guides/Guides/pull/2429) |
| FMD | Does Netflix mobile 480p releases and mislabels them with non-standard resolutions like 396p. | [#2338](https://github.com/TRaSH-Guides/Guides/pull/2338) |
| FRDS | Not documented | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| FS | Low-quality group, similar to SyncUP. | [#2801](https://github.com/TRaSH-Guides/Guides/pull/2801) |
| FZHD | Bad naming, wrong or incorrect info, frequent playback issues with audio and video, and fake 4K (re-graded or upscaled). | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#528](https://github.com/TRaSH-Guides/Guides/pull/528) re-added |
| GalaxyRG | Also added to LQ (Release Title), as some releases are badly formatted. | [#640](https://github.com/TRaSH-Guides/Guides/pull/640), [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) |
| GHD | Flagged for wrongly naming their files. | [#1302](https://github.com/TRaSH-Guides/Guides/pull/1302) |
| GHOSTS | 2.0 audio and odd frame rates. | Sonarr LQ: `52b372e6` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| GPTHD | Filenames are improperly formatted, and subtitles are hardcoded in Chinese. | [#1243](https://github.com/TRaSH-Guides/Guides/pull/1243) |
| GuyZo | Generated Dynamic HDR | [#2653](https://github.com/TRaSH-Guides/Guides/pull/2653) |
| HDHUB4U | Quality | [#2404](https://github.com/TRaSH-Guides/Guides/pull/2404) |
| HDS | Not documented | [#640](https://github.com/TRaSH-Guides/Guides/pull/640) |
| HDT | Does not add anything of value. Releases are run straight through MKVToolNix automatically with no checks, then dumped, a bump and dump group; Automated Remuxes, often lacking EN Subtitles | [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
| HDTime | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| HDWinG | Not documented | `ede09001` (direct commit) |
| HHWEB (No MA) | We received multiple reports that their releases often include hardcoded subtitles. All of these reports concern non-MA WEB-DL releases. | [#2682](https://github.com/TRaSH-Guides/Guides/pull/2682) |
| HiQVE | Does x265 encodes with their tag hardcoded in the top right, acting as a watermark; ENCODEs | [#1280](https://github.com/TRaSH-Guides/Guides/pull/1280) |
| iNTENSO | 4K/HDR releases where no HDR release is available. | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
| iPlanet | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| iVy | Quality; ENCODEs | [#1840](https://github.com/TRaSH-Guides/Guides/pull/1840) |
| jennaortega | The movie has no IMAX release with DV, and the disc master is DTS-HD MA, not TrueHD; also matched in LQ (Release Title) to catch releases with an extra space after the `-`. | [#1557](https://github.com/TRaSH-Guides/Guides/pull/1557), [#1659](https://github.com/TRaSH-Guides/Guides/pull/1659) |
| JFF | Microsized releases; Automated transcodes; (re-encoded WEB-DLs) | [#1125](https://github.com/TRaSH-Guides/Guides/pull/1125) |
| KC | Uses "Ai" ambiguously in release titles. | [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) |
| KiNGDOM | Quality; Intentionally misleading titles. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| KIRA | Wrong main audio track in the filename. | [#576](https://github.com/TRaSH-Guides/Guides/pull/576) |
| L0SERNIGHT | Reported by a user as a group that should be blocked. | [#841](https://github.com/TRaSH-Guides/Guides/pull/841) |
| LAMA | Uploads 480p cam rips as 1080p Blu-ray, generally low quality; ALL Re-Tagging; ENCODEs; automated low quality transcodes | [#1199](https://github.com/TRaSH-Guides/Guides/pull/1199) |
| Leffe | Not documented | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| Liber8 | Bad named BR-DISK releases. | [#511](https://github.com/TRaSH-Guides/Guides/pull/511) |
| LiGaS | Renamed and modified RARBG. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| LUCY | CAM releases labeled as WEB-DL. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
| MarkII | Micro-encoded releases with extra audio tracks that hurt video quality further because of the file size; does not mark the HDR fallback, so releases are badly named. Example: a 4.5 GB file for a 4K release with DV and HDR10 fallback. | [#1752](https://github.com/TRaSH-Guides/Guides/pull/1752) |
| MeGusta | Microsized releases; Quality; ENCODEs | [#333](https://github.com/TRaSH-Guides/Guides/pull/333), [#946](https://github.com/TRaSH-Guides/Guides/pull/946) |
| Mesc | Offers RiffTrax releases and produces AI upscale releases. | [#2582](https://github.com/TRaSH-Guides/Guides/pull/2582) |
| mHD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| mSD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| MTeam | Not documented. `MT` is matched as the shortened name of MTeam. | Radarr LQ: `ede09001` (direct commit) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
| MySiLU | Not documented | `ede09001` (direct commit) |
| NhaNc3 | Re-encodes from lower-quality releases. | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide)<br>Sonarr LQ: [#172](https://github.com/TRaSH-Guides/Guides/pull/172) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| nHD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| nikt0 | Microsized releases; All Low quality \| Poorly cropped \| Re-encodes | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| NoGroup | A generic name used for user releases on their respective tracker. | [#640](https://github.com/TRaSH-Guides/Guides/pull/640) |
| nSD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| OFT | They are a continuation group of nikt0, though OFT actually crops its encodes. Already banned on sites like PTP and ATH; ALL Bit starved encodes, connected to nikt0; All Low Quality - Same group as nikt0 | [#1344](https://github.com/TRaSH-Guides/Guides/pull/1344), [#2010](https://github.com/TRaSH-Guides/Guides/pull/2010) |
| OldT | Their multi-language releases do not set the original audio language as the first or default audio track. Their releases consistently list audio tracks alphabetically for both shows and movies instead of sorting them by language priority. As a result, languages like Arabic or Czech may appear first even when they are not the original language. | [#2856](https://github.com/TRaSH-Guides/Guides/pull/2856) |
| Pahe | Re-encoded, microsized releases (Pahe.ph and Pahe.in). | Radarr LQ: [#1325](https://github.com/TRaSH-Guides/Guides/pull/1325) added<br>Sonarr LQ: [#581](https://github.com/TRaSH-Guides/Guides/pull/581) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| PATOMiEL | Bad naming. | `add9ad8b` (direct commit) |
| PiRaTeS (no WEBDL) | Their encodes are low quality (artifacting in dark scenes). A user reported that they use custom discs as a source, from Triton and SPHD. | Radarr LQ: [#1161](https://github.com/TRaSH-Guides/Guides/pull/1161) added → [#2385](https://github.com/TRaSH-Guides/Guides/pull/2385) moved to LQ (Release Title)<br>Radarr LQ (Release Title): [#2385](https://github.com/TRaSH-Guides/Guides/pull/2385) moved from LQ |
| PRODJi | Releases seem low quality, with artifacting in dark scenes | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| PSA | Microsized releases; Quality; Pre-retail releases; ENCODEs | [#665](https://github.com/TRaSH-Guides/Guides/pull/665), [#1125](https://github.com/TRaSH-Guides/Guides/pull/1125) |
| PTNK | Uses mixed sources such as EVO releases, hardcodes Blu-ray subtitles, and strips out all other subtitles. | [#585](https://github.com/TRaSH-Guides/Guides/pull/585) |
| R&H | Known to create fake DV/HDR10(+). Not in Generated Dynamic HDR because they also release static HDR10. Matched in LQ (Release Title) because the Starr apps do not parse the `R&H` release group name properly. | Radarr + Sonarr LQ: [#2701](https://github.com/TRaSH-Guides/Guides/pull/2701) added → [#2767](https://github.com/TRaSH-Guides/Guides/pull/2767) moved to LQ (Release Title)<br>Radarr + Sonarr LQ (Release Title): [#2767](https://github.com/TRaSH-Guides/Guides/pull/2767) moved from LQ |
| RARBG | Microsized releases; ENCODEs; All Low Quality \| Stolen / Retagging; They rename other groups' releases and add an unwanted popup at the beginning. | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
| RBB | Tagged as WEB but are actually CAM recordings from cinemas. | [#2779](https://github.com/TRaSH-Guides/Guides/pull/2779) |
| RDN | Not documented | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| READ NOTE | Low-quality releases labeled as high quality, shipped with a note file. | [#2406](https://github.com/TRaSH-Guides/Guides/pull/2406) |
| RiffTrax | RiffTrax releases. | Radarr LQ: [#153](https://github.com/TRaSH-Guides/Guides/pull/153) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
| RU4HD | non-retail audio | Radarr LQ: [#178](https://github.com/TRaSH-Guides/Guides/pull/178) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
| SANTi | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| SasukeducK | Generated Dynamic HDR; non-retail audio; pre-retail | Radarr LQ: [#1832](https://github.com/TRaSH-Guides/Guides/pull/1832) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ: [#1832](https://github.com/TRaSH-Guides/Guides/pull/1832) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
| Scene | Adding "-scene" as an inline suffix to a media file name tells Plex to treat the file as a special extra, specifically a "Scene" bonus feature for that movie or episode. | [#328](https://github.com/TRaSH-Guides/Guides/pull/328), [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
| SHD | Incorrect DV profile usage and incompatible file containers (.ts). | [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) |
| ShieldBearer | ENCODEs | [#1911](https://github.com/TRaSH-Guides/Guides/pull/1911) |
| STUTTERSHIT | All Low quality \| Re-encoded; Another RARBG group which renames the hardcoded rips. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| SUNSCREEN | CAM releases labeled as WEB-DL, filled with advertisements, including floating text, clips between scenes, and large graphics. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
| SWTYBLZ | Copy-pastes encode settings, quality issues, and is associated with RARBG | Radarr LQ: [#707](https://github.com/TRaSH-Guides/Guides/pull/707) added → [#1967](https://github.com/TRaSH-Guides/Guides/pull/1967) moved to LQ (Release Title)<br>Radarr LQ (Release Title): [#1967](https://github.com/TRaSH-Guides/Guides/pull/1967) moved from LQ |
| SyncUP | Low-quality pre-releases (Telesync, CAM, or mislabeled as WEB or WEB-DL), frequently sourced from unknown or CAM sources with the wrong quality in the release title; Pre-retail releases | [#2801](https://github.com/TRaSH-Guides/Guides/pull/2801) |
| tarunk9c | Uses non-retail Dolby Vision and HDR10+ layers generated with DaVinci Resolve; Generated Dynamic HDR | Radarr LQ: [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
| TBS | Mislabeled or stripped/re-encoded releases. | Radarr LQ: [#333](https://github.com/TRaSH-Guides/Guides/pull/333) added<br>Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| TeeWee | Azerbaijani dubs with screen overlays. | [#1639](https://github.com/TRaSH-Guides/Guides/pull/1639) |
| TEKNO3D | Inconsistent naming scheme, so releases were not always recognized as a release group; they have requested their torrents are not shared off site. | [#498](https://github.com/TRaSH-Guides/Guides/pull/498), [#1956](https://github.com/TRaSH-Guides/Guides/pull/1956) |
| TG | They release in strange aspect ratios and mislabel their releases. | [#1299](https://github.com/TRaSH-Guides/Guides/pull/1299) |
| Tigole | Microsized releases; part of QxR | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| TIKO | Not documented | [#498](https://github.com/TRaSH-Guides/Guides/pull/498) |
| UnKn0wn (NoRemux) | Used as a generic RlsGrp by some trackers. | [#2700](https://github.com/TRaSH-Guides/Guides/pull/2700) |
| VD0N | Generated Dynamic HDR | [#2325](https://github.com/TRaSH-Guides/Guides/pull/2325) |
| VECTOR | Generated Dynamic HDR, via user-generated dynamic HDR metadata made with DaVinci Resolve. | Radarr LQ: [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
| VIDEOHOLE | Same quality as TBS, with AAC 2.0 audio. | Sonarr LQ: `62c19ea3` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| VISIONPLUSHDR | Fake HDR releases. | [#1447](https://github.com/TRaSH-Guides/Guides/pull/1447) |
| VisionXpert | Generated Dynamic HDR | [#2567](https://github.com/TRaSH-Guides/Guides/pull/2567) |
| WAF | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| WiKi | Not documented | `ede09001` (direct commit) |
| Will1869 | Quality | [#1702](https://github.com/TRaSH-Guides/Guides/pull/1702) |
| worldmkv | Microsized releases (a 1080p WEB-DL of 530 MB). | Sonarr LQ: `2f281eba` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| x0r | All Low quality \| Poorly cropped \| Re-encodes | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
| XLF | Lower-quality releases; some of their releases are encodes and not real WEB-DLs (the new TBS). | Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
| YIFY | Microsized releases; All Low quality \| Poorly cropped \| Re-encodes | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
| YTS | Microsized releases; Quality; ENCODEs | Radarr LQ: [#12](https://github.com/TRaSH-Guides/Guides/pull/12) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
| Zero00 | Upscaled DVD to 720p (e.g., Star Trek Voyager) without mentioning it in the name. | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
| Zeus | Uses mono/strereo audio on UHD releases and has a history of upscaling from 1080p. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |

## By Custom Format

The same groups, split by Custom Format. A group in more than one appears in more than one tab. Radarr and Sonarr versions of the same Custom Format are combined.

=== "LQ"

    | RlsGrp | Reason | PR |
    | --- | --- | --- |
    | 126811 | Hit-or-miss on including the release group name, which can disrupt automation due to poor naming; non-retail audio; Generated Dynamic HDR; Hybrids without grade checks. | [#2895](https://github.com/TRaSH-Guides/Guides/pull/2895) |
    | 24xHD | They don't include the used codec in the file or release name. | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
    | 41RGB | Uses the wrong audio formats in the release name. | [#1533](https://github.com/TRaSH-Guides/Guides/pull/1533) |
    | 4K4U | Quality. | [#333](https://github.com/TRaSH-Guides/Guides/pull/333) |
    | AOC | Releases are TS/CAM rips that are badly named, leading to incorrect ranking; Pre-retail releases | [#2396](https://github.com/TRaSH-Guides/Guides/pull/2396) |
    | AROMA | ALL Re-Tagging | [#333](https://github.com/TRaSH-Guides/Guides/pull/333) |
    | aXXo | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | AZAZE | 4K Dolby Vision IMAX Blu-ray encodes that do not include an HDR10 fallback. | [#1162](https://github.com/TRaSH-Guides/Guides/pull/1162) |
    | BARC0DE | Not documented | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#468](https://github.com/TRaSH-Guides/Guides/pull/468) re-added |
    | BAUCKLEY | Bad audio, gore scenes are cut, and odd alcohol warnings appear throughout the movie. The audio track is also sometimes mislabeled as Hindi for no clear reason. | [#2168](https://github.com/TRaSH-Guides/Guides/pull/2168) |
    | BdC | Not documented | [#640](https://github.com/TRaSH-Guides/Guides/pull/640) |
    | beAst | Not documented | `ede09001` (direct commit) |
    | BRiNK | Not documented | Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | BTM | Release titles do not format the release group name properly or include the quality (for example Blu-ray or WEB-DL), which breaks automation. | [#2377](https://github.com/TRaSH-Guides/Guides/pull/2377) |
    | C1NEM4 | CAM releases labeled as WEB-DL, filled with advertisements, including floating text, clips between scenes, and large graphics. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
    | C4K | Not documented | [#333](https://github.com/TRaSH-Guides/Guides/pull/333) |
    | CDDHD | Not documented | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#468](https://github.com/TRaSH-Guides/Guides/pull/468) re-added |
    | CHAOS | Not documented | [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
    | CHD | Not documented | Radarr LQ: `ede09001` (direct commit) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
    | CHX | Not documented | Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | CiNE | Fake releases: labeled as the new Spider-Man (Across the Spider-Verse) but actually the old movie. | [#1352](https://github.com/TRaSH-Guides/Guides/pull/1352) |
    | CLEANUP | Low-quality group, similar to SyncUP (name-dropped in SyncUP release notes as an affiliated low-quality group). | [#2801](https://github.com/TRaSH-Guides/Guides/pull/2801) |
    | COLLECTiVE | CAM releases labeled as WEB-DL. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
    | CREATiVE24 | Quality | [#1068](https://github.com/TRaSH-Guides/Guides/pull/1068), [#2274](https://github.com/TRaSH-Guides/Guides/pull/2274) |
    | CrEwSaDe | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | CTFOH | 4K/HDR releases where no HDR release is available; Quality | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
    | d3g | Microsized releases; All Low quality \| Hardware encodes | [#333](https://github.com/TRaSH-Guides/Guides/pull/333), [#1562](https://github.com/TRaSH-Guides/Guides/pull/1562) |
    | DDR | Renames UHDClub's releases. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | DepraveD | Generated Dynamic HDR; also added to Sonarr LQ, as some TV releases were identified too. | Radarr LQ: [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ: [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
    | DNL | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | DRX | Uses non-retail audio; Quality | [#2466](https://github.com/TRaSH-Guides/Guides/pull/2466) |
    | E | User-generated Atmos, poorly named files, upmixed audio. | [#2436](https://github.com/TRaSH-Guides/Guides/pull/2436) |
    | EPiC | Wrong audio format listed in the release name. | [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
    | EuReKA | Not documented | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#468](https://github.com/TRaSH-Guides/Guides/pull/468) re-added |
    | EVO | Often banned for low-quality Blu-ray releases (EVO (no WEBDL) description in the Radarr guide). | [#610](https://github.com/TRaSH-Guides/Guides/pull/610) |
    | FaNGDiNG0 | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | Feranki1980 | Low-quality, microsized releases. | [#2320](https://github.com/TRaSH-Guides/Guides/pull/2320) |
    | FGT | Bloated with unnecessary audio tracks, re-tagging; ALL Re-Tagging; unless no other encode is available; All Low Quality \| Bloated Releases; (Movie WEB-DLs allowed)- Sister group of RARBG. Same ethics and practices. | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added<br>Sonarr LQ: [#1007](https://github.com/TRaSH-Guides/Guides/pull/1007) added |
    | FMD | Does Netflix mobile 480p releases and mislabels them with non-standard resolutions like 396p. | [#2338](https://github.com/TRaSH-Guides/Guides/pull/2338) |
    | FRDS | Not documented | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | FS | Low-quality group, similar to SyncUP. | [#2801](https://github.com/TRaSH-Guides/Guides/pull/2801) |
    | FZHD | Bad naming, wrong or incorrect info, frequent playback issues with audio and video, and fake 4K (re-graded or upscaled). | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) removed → [#528](https://github.com/TRaSH-Guides/Guides/pull/528) re-added |
    | GalaxyRG | Also added to LQ (Release Title), as some releases are badly formatted. | [#640](https://github.com/TRaSH-Guides/Guides/pull/640), [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) |
    | GHD | Flagged for wrongly naming their files. | [#1302](https://github.com/TRaSH-Guides/Guides/pull/1302) |
    | GHOSTS | 2.0 audio and odd frame rates. | Sonarr LQ: `52b372e6` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | GPTHD | Filenames are improperly formatted, and subtitles are hardcoded in Chinese. | [#1243](https://github.com/TRaSH-Guides/Guides/pull/1243) |
    | HDHUB4U | Quality | [#2404](https://github.com/TRaSH-Guides/Guides/pull/2404) |
    | HDS | Not documented | [#640](https://github.com/TRaSH-Guides/Guides/pull/640) |
    | HDT | Does not add anything of value. Releases are run straight through MKVToolNix automatically with no checks, then dumped, a bump and dump group; Automated Remuxes, often lacking EN Subtitles | [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
    | HDTime | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | HDWinG | Not documented | `ede09001` (direct commit) |
    | HiQVE | Does x265 encodes with their tag hardcoded in the top right, acting as a watermark; ENCODEs | [#1280](https://github.com/TRaSH-Guides/Guides/pull/1280) |
    | iNTENSO | 4K/HDR releases where no HDR release is available. | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
    | iPlanet | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | iVy | Quality; ENCODEs | [#1840](https://github.com/TRaSH-Guides/Guides/pull/1840) |
    | jennaortega | The movie has no IMAX release with DV, and the disc master is DTS-HD MA, not TrueHD; also matched in LQ (Release Title) to catch releases with an extra space after the `-`. | [#1557](https://github.com/TRaSH-Guides/Guides/pull/1557), [#1659](https://github.com/TRaSH-Guides/Guides/pull/1659) |
    | JFF | Microsized releases; Automated transcodes; (re-encoded WEB-DLs) | [#1125](https://github.com/TRaSH-Guides/Guides/pull/1125) |
    | KC | Uses "Ai" ambiguously in release titles. | [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) |
    | KiNGDOM | Quality; Intentionally misleading titles. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | KIRA | Wrong main audio track in the filename. | [#576](https://github.com/TRaSH-Guides/Guides/pull/576) |
    | L0SERNIGHT | Reported by a user as a group that should be blocked. | [#841](https://github.com/TRaSH-Guides/Guides/pull/841) |
    | LAMA | Uploads 480p cam rips as 1080p Blu-ray, generally low quality; ALL Re-Tagging; ENCODEs; automated low quality transcodes | [#1199](https://github.com/TRaSH-Guides/Guides/pull/1199) |
    | Leffe | Not documented | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | Liber8 | Bad named BR-DISK releases. | [#511](https://github.com/TRaSH-Guides/Guides/pull/511) |
    | LiGaS | Renamed and modified RARBG. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | LUCY | CAM releases labeled as WEB-DL. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
    | MarkII | Micro-encoded releases with extra audio tracks that hurt video quality further because of the file size; does not mark the HDR fallback, so releases are badly named. Example: a 4.5 GB file for a 4K release with DV and HDR10 fallback. | [#1752](https://github.com/TRaSH-Guides/Guides/pull/1752) |
    | MeGusta | Microsized releases; Quality; ENCODEs | [#333](https://github.com/TRaSH-Guides/Guides/pull/333), [#946](https://github.com/TRaSH-Guides/Guides/pull/946) |
    | Mesc | Offers RiffTrax releases and produces AI upscale releases. | [#2582](https://github.com/TRaSH-Guides/Guides/pull/2582) |
    | mHD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | mSD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | MTeam | Not documented. `MT` is matched as the shortened name of MTeam. | Radarr LQ: `ede09001` (direct commit) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
    | MySiLU | Not documented | `ede09001` (direct commit) |
    | NhaNc3 | Re-encodes from lower-quality releases. | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide)<br>Sonarr LQ: [#172](https://github.com/TRaSH-Guides/Guides/pull/172) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | nHD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | nikt0 | Microsized releases; All Low quality \| Poorly cropped \| Re-encodes | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | NoGroup | A generic name used for user releases on their respective tracker. | [#640](https://github.com/TRaSH-Guides/Guides/pull/640) |
    | nSD | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | OFT | They are a continuation group of nikt0, though OFT actually crops its encodes. Already banned on sites like PTP and ATH; ALL Bit starved encodes, connected to nikt0; All Low Quality - Same group as nikt0 | [#1344](https://github.com/TRaSH-Guides/Guides/pull/1344), [#2010](https://github.com/TRaSH-Guides/Guides/pull/2010) |
    | Pahe | Re-encoded, microsized releases (Pahe.ph and Pahe.in). | Radarr LQ: [#1325](https://github.com/TRaSH-Guides/Guides/pull/1325) added<br>Sonarr LQ: [#581](https://github.com/TRaSH-Guides/Guides/pull/581) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | PATOMiEL | Bad naming. | `add9ad8b` (direct commit) |
    | PRODJi | Releases seem low quality, with artifacting in dark scenes | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | PSA | Microsized releases; Quality; Pre-retail releases; ENCODEs | [#665](https://github.com/TRaSH-Guides/Guides/pull/665), [#1125](https://github.com/TRaSH-Guides/Guides/pull/1125) |
    | PTNK | Uses mixed sources such as EVO releases, hardcodes Blu-ray subtitles, and strips out all other subtitles. | [#585](https://github.com/TRaSH-Guides/Guides/pull/585) |
    | RARBG | Microsized releases; ENCODEs; All Low Quality \| Stolen / Retagging; They rename other groups' releases and add an unwanted popup at the beginning. | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
    | RBB | Tagged as WEB but are actually CAM recordings from cinemas. | [#2779](https://github.com/TRaSH-Guides/Guides/pull/2779) |
    | RDN | Not documented | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | RiffTrax | RiffTrax releases. | Radarr LQ: [#153](https://github.com/TRaSH-Guides/Guides/pull/153) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
    | RU4HD | non-retail audio | Radarr LQ: [#178](https://github.com/TRaSH-Guides/Guides/pull/178) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
    | SANTi | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | SasukeducK | Generated Dynamic HDR; non-retail audio; pre-retail | Radarr LQ: [#1832](https://github.com/TRaSH-Guides/Guides/pull/1832) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ: [#1832](https://github.com/TRaSH-Guides/Guides/pull/1832) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
    | Scene | Adding "-scene" as an inline suffix to a media file name tells Plex to treat the file as a special extra, specifically a "Scene" bonus feature for that movie or episode. | [#328](https://github.com/TRaSH-Guides/Guides/pull/328), [#707](https://github.com/TRaSH-Guides/Guides/pull/707) |
    | SHD | Incorrect DV profile usage and incompatible file containers (.ts). | [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) |
    | ShieldBearer | ENCODEs | [#1911](https://github.com/TRaSH-Guides/Guides/pull/1911) |
    | STUTTERSHIT | All Low quality \| Re-encoded; Another RARBG group which renames the hardcoded rips. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | SUNSCREEN | CAM releases labeled as WEB-DL, filled with advertisements, including floating text, clips between scenes, and large graphics. | [#2205](https://github.com/TRaSH-Guides/Guides/pull/2205) |
    | SyncUP | Low-quality pre-releases (Telesync, CAM, or mislabeled as WEB or WEB-DL), frequently sourced from unknown or CAM sources with the wrong quality in the release title; Pre-retail releases | [#2801](https://github.com/TRaSH-Guides/Guides/pull/2801) |
    | TBS | Mislabeled or stripped/re-encoded releases. | Radarr LQ: [#333](https://github.com/TRaSH-Guides/Guides/pull/333) added<br>Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | TEKNO3D | Inconsistent naming scheme, so releases were not always recognized as a release group; they have requested their torrents are not shared off site. | [#498](https://github.com/TRaSH-Guides/Guides/pull/498), [#1956](https://github.com/TRaSH-Guides/Guides/pull/1956) |
    | TG | They release in strange aspect ratios and mislabel their releases. | [#1299](https://github.com/TRaSH-Guides/Guides/pull/1299) |
    | Tigole | Microsized releases; part of QxR | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | TIKO | Not documented | [#498](https://github.com/TRaSH-Guides/Guides/pull/498) |
    | VIDEOHOLE | Same quality as TBS, with AAC 2.0 audio. | Sonarr LQ: `62c19ea3` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | VISIONPLUSHDR | Fake HDR releases. | [#1447](https://github.com/TRaSH-Guides/Guides/pull/1447) |
    | WAF | Quality | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | WiKi | Not documented | `ede09001` (direct commit) |
    | worldmkv | Microsized releases (a 1080p WEB-DL of 530 MB). | Sonarr LQ: `2f281eba` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | x0r | All Low quality \| Poorly cropped \| Re-encodes | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |
    | XLF | Lower-quality releases; some of their releases are encodes and not real WEB-DLs (the new TBS). | Sonarr LQ: `31ac6309` (direct commit) added (Sonarr release profile) → [#596](https://github.com/TRaSH-Guides/Guides/pull/596) added as a custom format → [#597](https://github.com/TRaSH-Guides/Guides/pull/597) removed → [#598](https://github.com/TRaSH-Guides/Guides/pull/598) re-added → `f6b87d5e` (direct commit) removed → [#610](https://github.com/TRaSH-Guides/Guides/pull/610) re-added |
    | YIFY | Microsized releases; All Low quality \| Poorly cropped \| Re-encodes | Radarr LQ: [#9](https://github.com/TRaSH-Guides/Guides/pull/9) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
    | YTS | Microsized releases; Quality; ENCODEs | Radarr LQ: [#12](https://github.com/TRaSH-Guides/Guides/pull/12) added (Radarr guide) → [#236](https://github.com/TRaSH-Guides/Guides/pull/236) removed (dropped in the JSON conversion) → [#333](https://github.com/TRaSH-Guides/Guides/pull/333) re-added |
    | Zero00 | Upscaled DVD to 720p (e.g., Star Trek Voyager) without mentioning it in the name. | [#1508](https://github.com/TRaSH-Guides/Guides/pull/1508) |
    | Zeus | Uses mono/strereo audio on UHD releases and has a history of upscaling from 1080p. | [#9](https://github.com/TRaSH-Guides/Guides/pull/9) |

=== "LQ (Release Title)"

    | RlsGrp | Reason | PR |
    | --- | --- | --- |
    | 1XBET | Releases contain adverts and watermarks. | [#1679](https://github.com/TRaSH-Guides/Guides/pull/1679) |
    | BEN THE MEN | Releases are badly named and do not include the quality (WEB, Blu-ray, and so on), which breaks automation; low quality. | [#1773](https://github.com/TRaSH-Guides/Guides/pull/1773) |
    | BiTOR (2160p) | Generated Dynamic HDR; ENCODEs; non-retail audio; 2160p releases added to LQ (Release Title); 1080p releases are untiered rather than banned. | Radarr LQ: [#1048](https://github.com/TRaSH-Guides/Guides/pull/1048) added → [#1607](https://github.com/TRaSH-Guides/Guides/pull/1607) removed<br>Radarr LQ (Release Title): [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ (Release Title): [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ (Release Title) |
    | CREATiVE24 | Quality | [#1068](https://github.com/TRaSH-Guides/Guides/pull/1068), [#2274](https://github.com/TRaSH-Guides/Guides/pull/2274) |
    | D3US | Release names do not follow naming conventions, so they cannot be reliably parsed. | [#2439](https://github.com/TRaSH-Guides/Guides/pull/2439) |
    | EVO (no WEBDL) | Encode, Quality; encodes: BluRay & WEBRip (WEB-DL are okay); WEBs / ENCODEs; Encode Quality; WEB-DLs are allowed | Radarr LQ: [#640](https://github.com/TRaSH-Guides/Guides/pull/640) added → [#664](https://github.com/TRaSH-Guides/Guides/pull/664) removed (EVO moves to its own EVO (no WEBDL) CF)<br>Radarr LQ (Release Title): [#2386](https://github.com/TRaSH-Guides/Guides/pull/2386) moved from the EVO (no WEBDL) CF |
    | Feranki1980 | Low-quality, microsized releases. | [#2320](https://github.com/TRaSH-Guides/Guides/pull/2320) |
    | GalaxyRG | Also added to LQ (Release Title), as some releases are badly formatted. | [#640](https://github.com/TRaSH-Guides/Guides/pull/640), [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) |
    | HHWEB (No MA) | We received multiple reports that their releases often include hardcoded subtitles. All of these reports concern non-MA WEB-DL releases. | [#2682](https://github.com/TRaSH-Guides/Guides/pull/2682) |
    | jennaortega | The movie has no IMAX release with DV, and the disc master is DTS-HD MA, not TrueHD; also matched in LQ (Release Title) to catch releases with an extra space after the `-`. | [#1557](https://github.com/TRaSH-Guides/Guides/pull/1557), [#1659](https://github.com/TRaSH-Guides/Guides/pull/1659) |
    | PiRaTeS (no WEBDL) | Their encodes are low quality (artifacting in dark scenes). A user reported that they use custom discs as a source, from Triton and SPHD. | Radarr LQ: [#1161](https://github.com/TRaSH-Guides/Guides/pull/1161) added → [#2385](https://github.com/TRaSH-Guides/Guides/pull/2385) moved to LQ (Release Title)<br>Radarr LQ (Release Title): [#2385](https://github.com/TRaSH-Guides/Guides/pull/2385) moved from LQ |
    | R&H | Known to create fake DV/HDR10(+). Not in Generated Dynamic HDR because they also release static HDR10. Matched in LQ (Release Title) because the Starr apps do not parse the `R&H` release group name properly. | Radarr + Sonarr LQ: [#2701](https://github.com/TRaSH-Guides/Guides/pull/2701) added → [#2767](https://github.com/TRaSH-Guides/Guides/pull/2767) moved to LQ (Release Title)<br>Radarr + Sonarr LQ (Release Title): [#2767](https://github.com/TRaSH-Guides/Guides/pull/2767) moved from LQ |
    | READ NOTE | Low-quality releases labeled as high quality, shipped with a note file. | [#2406](https://github.com/TRaSH-Guides/Guides/pull/2406) |
    | SWTYBLZ | Copy-pastes encode settings, quality issues, and is associated with RARBG | Radarr LQ: [#707](https://github.com/TRaSH-Guides/Guides/pull/707) added → [#1967](https://github.com/TRaSH-Guides/Guides/pull/1967) moved to LQ (Release Title)<br>Radarr LQ (Release Title): [#1967](https://github.com/TRaSH-Guides/Guides/pull/1967) moved from LQ |
    | TeeWee | Azerbaijani dubs with screen overlays. | [#1639](https://github.com/TRaSH-Guides/Guides/pull/1639) |
    | TEKNO3D | Inconsistent naming scheme, so releases were not always recognized as a release group; they have requested their torrents are not shared off site. | [#498](https://github.com/TRaSH-Guides/Guides/pull/498), [#1956](https://github.com/TRaSH-Guides/Guides/pull/1956) |
    | UnKn0wn (NoRemux) | Used as a generic RlsGrp by some trackers. | [#2700](https://github.com/TRaSH-Guides/Guides/pull/2700) |
    | Will1869 | Quality | [#1702](https://github.com/TRaSH-Guides/Guides/pull/1702) |

=== "Generated Dynamic HDR"

    | RlsGrp | Reason | PR |
    | --- | --- | --- |
    | BiTOR | Generated Dynamic HDR; ENCODEs; non-retail audio; 2160p releases added to LQ (Release Title); 1080p releases are untiered rather than banned. | Radarr LQ: [#1048](https://github.com/TRaSH-Guides/Guides/pull/1048) added → [#1607](https://github.com/TRaSH-Guides/Guides/pull/1607) removed<br>Radarr LQ (Release Title): [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ (Release Title): [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ (Release Title) |
    | DepraveD | Generated Dynamic HDR; also added to Sonarr LQ, as some TV releases were identified too. | Radarr LQ: [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ: [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
    | Flights | Generated Dynamic HDR | [#2429](https://github.com/TRaSH-Guides/Guides/pull/2429) |
    | GuyZo | Generated Dynamic HDR | [#2653](https://github.com/TRaSH-Guides/Guides/pull/2653) |
    | SasukeducK | Generated Dynamic HDR; non-retail audio; pre-retail | Radarr LQ: [#1832](https://github.com/TRaSH-Guides/Guides/pull/1832) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Sonarr LQ: [#1832](https://github.com/TRaSH-Guides/Guides/pull/1832) added<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
    | tarunk9c | Uses non-retail Dolby Vision and HDR10+ layers generated with DaVinci Resolve; Generated Dynamic HDR | Radarr LQ: [#1644](https://github.com/TRaSH-Guides/Guides/pull/1644) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
    | VD0N | Generated Dynamic HDR | [#2325](https://github.com/TRaSH-Guides/Guides/pull/2325) |
    | VECTOR | Generated Dynamic HDR, via user-generated dynamic HDR metadata made with DaVinci Resolve. | Radarr LQ: [#2023](https://github.com/TRaSH-Guides/Guides/pull/2023) added → [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved to Generated Dynamic HDR<br>Radarr Generated Dynamic HDR: [#2185](https://github.com/TRaSH-Guides/Guides/pull/2185) moved from LQ |
    | VisionXpert | Generated Dynamic HDR | [#2567](https://github.com/TRaSH-Guides/Guides/pull/2567) |
