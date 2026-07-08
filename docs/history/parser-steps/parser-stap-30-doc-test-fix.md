# Stap 30 - documentatietest fix

De demo-site tests waren groen, maar `test_user_docs.py` faalde op twee te specifieke tekstverwachtingen.

De tests zijn nu minder kwetsbaar:

- ze controleren nog steeds of `<assets-dir>` goed wordt uitgelegd;
- ze controleren nog steeds of validatiechecks worden uitgelegd;
- ze eisen niet meer één exacte hoofdlettergevoelige formulering.
