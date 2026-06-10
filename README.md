# VSA stap 24 - GitHub Actions opschonen

Deze stap maakt de GitHub Actions duidelijker.

Er zijn nu twee workflows:

```text
VSA CI
  = Windows, CMD, scripts\ci.cmd

Hugo demo build
  = Ubuntu, Python, VSA build-markdown, Hugo build
```

Waarom:

- tool-CI blijft dicht bij jouw Windows/CMD workflow;
- Hugo-build gebruikt Linux, zoals veel hosting/deploy workflows;
- fouten worden makkelijker te lokaliseren.
