<!--
============================================================================
 HOW TO KEEP THIS UP TO DATE
============================================================================
 Adding a new disclosure, cert, or job? Two places to touch:

 1) The markdown sections below (## Vulnerability Research, ## Certifications,
    etc.) -- just add a new bullet/block. No tools needed, plain text edit.

 2) The banner image at the top (assets/profile-card.svg) is generated from
    scripts/build_card.py. Open that file, add a matching line to the ITEMS
    list near the top (each block has an "ADD-NEW-..." comment marking where),
    then run:
        pip install pillow --break-system-packages
        python3 scripts/build_card.py
    and commit the updated assets/profile-card.svg. Swapping scripts/photo.png
    and re-running also regenerates the ASCII portrait from a new photo.

 The GitHub stats section near the bottom is a live badge (github-readme-stats)
 keyed to your username -- it updates itself automatically, nothing to edit.
============================================================================
-->

<p align="center">
  <img src="./assets/profile-card.png" width="900" alt="Swornim Poudel — Cyber Security Analyst (VAPT)"/>
</p>

<h1 align="center">Swornim Poudel</h1>
<p align="center"><i>Cyber Security Analyst (VAPT) · Vulnerability Research</i></p>

<p align="center">
  <a href="mailto:pswor69@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white"/></a>
  <a href="https://www.linkedin.com/in/swornim-poudel-4a4721343"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/swornim619"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/></a>
  <a href="https://medium.com/@pswor69"><img src="https://img.shields.io/badge/Medium-000000?style=flat-square&logo=medium&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Location-Lalitpur%2C%20Nepal-6e7681?style=flat-square"/>
</p>

---

### About

Cybersecurity learner with hands-on VAPT experience and a track record of independently discovering and responsibly disclosing real-world vulnerabilities to major organizations including Mozilla, Google, and open-source security projects. Actively growing in offensive security, fuzzing, and secure system design.

---

### Things That Are True

- I Love My Laptop.

---

### 🎭 Transformation Sequence

<p align="center">
  <img src="./assets/venom_transform.gif" width="380" alt="Venom transformation"/>
  &nbsp;&nbsp;&nbsp;
  <img src="./assets/moonknight_transform.gif" width="380" alt="Moon Knight transformation"/>
</p>

<p align="center"><sub>Don't ask why. It just felt right.</sub></p>

---

### 🔎 Vulnerability Research & Responsible Disclosure

Independently discovered, reported, and helped resolve security vulnerabilities across separate real-world codebases through coordinated disclosure channels.

<!-- ADD-NEW-DISCLOSURE: copy a block below (heading + bullets) and fill in the new finding -->

**Mozilla Firefox — PDF.js Viewer** · Bugzilla [#2025109](https://bugzilla.mozilla.org/show_bug.cgi?id=2025109)
- Discovered a URL-spoofing / phishing flaw where PDF.js displayed raw annotation URLs instead of resolved hostnames, enabling userinfo-based hostname spoofing (e.g. `trusted.example@attacker.example`).
- Classified under `csectype-spoof` and escalated to the firefox-core-security group; fix landed in **Firefox 152** (`RESOLVED FIXED`).

**Google Guava — BloomFilter Deserialization DoS** · Google OSS VRP [PR # 15484](https://github.com/google/oss-fuzz/pull/15484)
- Identified an unbounded memory allocation bug in `BloomFilter.readFrom()`, where a 6-byte attacker-controlled input triggers an `OutOfMemoryError` and deterministic denial of service.
- Built a working PoC and authored a complete OSS-Fuzz target (`BloomFilterReadFromFuzzer`); fix (PR #8449) merged by a Google engineer, referencing the submitted fuzz target.
- Accepted into Google's OSS VRP program on a **Flagship (OT0-tier)** project.

**Elgg — Avatar Upload Denial of Service** · [CVE-2026-65650](https://nvd.nist.gov/vuln/detail/CVE-2026-65650)
- Reported a DoS (CWE-770) where Elgg failed to validate image dimensions on avatar uploads, enabling resource-exhaustion attacks.
- Published via MITRE CNA-LR; indexed in NVD and [GHSA-7983-35fr-8qwm](https://github.com/advisories/GHSA-7983-35fr-8qwm) — CVSS 3.1: 4.3 (Medium).

**OSSF Allstar — Broken Sort Comparator Bypassing Deny Rules** · [GHSA-r4gf-cmfp-wq5c](https://github.com/ossf/allstar/security/advisories/GHSA-r4gf-cmfp-wq5c)
- Found a comparator in Allstar's action-policy sort that violated basic ordering rules, letting lower-priority allow rules silently beat higher-priority deny rules with no error or warning.
- Root cause: `pkg/policies/action/action.go` — CWE-670. CVSS 3.1: 4.3 (Medium). Fixed in v4.6.

---

### 🛠️ Tools & Technologies

<p>
  <img src="https://img.shields.io/badge/Burp%20Suite-FF6633?style=flat-square&logo=burpsuite&logoColor=white"/>
  <img src="https://img.shields.io/badge/OSS--Fuzz-4285F4?style=flat-square&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/OWASP%20Top%2010-000000?style=flat-square&logo=owasp&logoColor=white"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"/>
  <img src="https://img.shields.io/badge/API%20Security-informational?style=flat-square"/>
  <img src="https://img.shields.io/badge/Fuzzing-informational?style=flat-square"/>
</p>

<!-- ADD-NEW-TOOL: add another badge line above, same format -->

---

### 📊 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=swornim619&show_icons=true&theme=dark&hide_border=true&bg_color=0d1117"/>
  <img height="165" src="https://github-readme-streak-stats.herokuapp.com/?user=swornim619&theme=dark&hide_border=true&background=0d1117"/>
</p>

---

### 📫 Contact

- **Email:** [pswor69@gmail.com](mailto:pswor69@gmail.com)
- **LinkedIn:** [swornim-poudel-4a4721343](https://www.linkedin.com/in/swornim-poudel-4a4721343)
- **GitHub:** [swornim619](https://github.com/swornim619)
- **Medium:** [@pswor69](https://medium.com/@pswor69)
- **Phone:** +977 9849782874
