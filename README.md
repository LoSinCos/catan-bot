# Catan Bot 
Creates catan game on colonist.io and sends the game link to slack

#### Dependancies
`selenium`  
`json`  
`requests`

## How to run
1. Install [Chromedriver](https://chromedriver.chromium.org/)
2. Create a [slack app](https://api.slack.com/apps)
3. Invite the slack app to a channel
4. Run the script with the path to the driver and the slack app URL as inputs

## How it works
1. The script opens an instance of Chrome.
2. Chrome goes the colonist.io website.
3. Clicks the `create game` button.
4. Makes the game private via the checkmark.
5. Once the game is private, sends the link to the game in the slack channel as the app.
6. The app then waits 2 minutes for someone to join, if no user joins the lobby, the app exits the game, closing the lobby.
7. Once someone joins, the app leaves the lobby, making the first person to join the new host and able to start the game.
8. The app then closes its instance.

