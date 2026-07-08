# Stap 45 - modifier count column fix

`VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH` werd nog op kolom 1 gemeld.

De helper die de mismatch-locatie zoekt gebruikt nu alleen de echte prefix van
het zangelement, in plaats van opnieuw te starten na elk tekstteken.
