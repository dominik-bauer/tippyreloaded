# TippyReloaded

### Overview

This is WebApp for a private betting game, in which we guess the final ranking tables of german football leagues. The WebApp is a reloaded version of the old TippyTippsen. The old version used a threema bot to send status updates to all players. The new version is a webapp, which is hosted on a webserver. The results are publicly available. The players can access/refresh the page and trigger an update of the results. The trigger starts a small scraping job, which fetches the current ranking tables from the sportschau.de website. The results are then displayed on the webapp. No need for databases, no need for expensive threema bots.

### List of open Points

```markdown
[ ] Add timestamp of the data: "Last Updated: "
[ ] Add detailed points overview per player/per team
[ ] Add badges to the website
[ ] Use str-Enums
[ ] Add rate limiting
[ ] Add clever way of reducing scraping job trigger and showing that information to the frontend (like wait time)
[ ] Switch to FastAPI for no reason
[ ] Switch to Django for learning purposes
[ ] Add fetch-API for updating the results or dynamically updating the quotes
[ ] Add "with this link" can edit/view/... functionality
```

### Rules of the betting Game

In this private betting game a number of players are guessing each, how the final ranking tables of any number of german leagues will look like after the current season. Typically we guess 1. Bundesliga & 2. Bundesliga. The player with the best guess wins. The best guess is determined by a simple points system:

- 3 Points for a team, whose rank was correctly guessed (diff: 0)
- 2 Points for a team, whose rank was almost certainly correctly guessed (diff: 1)
- 1 Point for a team, whose rank was almost correctly guessed (diff: 2)
- 0 Points for a team, whose rank was incorrectly guesses (diff > 2)

Say, Team A wins the season championship and is ranked in first position. If one predicted that Team A is first, 3 points are received. But if one predicted Team A in 2nd or 3rd or 4th position, accordingly 2 or 1 or 0 points are received.

### The Process creating the WebApp

1. Select the technology stack: Python, Flask, HTML, CSS, JavaScript
2. Select provider for the web hosting.
3. Determine the versions of the tech stack available at the hosting site.
4. Setup the local dev environment: python=3.10, flask=2.1.2, ...
5. Refactor and rebuild parts of the old TippyTippsen codebase.
6. Deploy the webapp to the hosting provider.
