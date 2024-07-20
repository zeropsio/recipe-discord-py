# Zerops x Discord.py

Discord.py is a powerful module that allows you to interact with the Discord API very easily. This is the most bare-bones example of [Discord.js](https://zerops.io) bot running on Zerops with a single ping command running on Python runtime.

![discordjs](https://github.com/zeropsio/recipe-shared-assets/blob/main/covers/svg/cover-discordpy.svg)

<br/>

## Deploy to Zerops

You can either click the deploy button to deploy directly on Zerops, or manually copy the [import yaml](https://github.com/zeropsio/recipe-discord-py/blob/main/zerops-project-import.yml) to the import dialog in the Zerops app.

<br/>

> [!WARNING]
> You'll encounter some runtime errors if `DISCORD_TOKEN` is not set in the environment variables.

<br/>

[![Deploy on Zerops](https://github.com/zeropsio/recipe-shared-assets/blob/main/deploy-button/green/deploy-button.svg)](https://app.zerops.io/recipe/discord-py)

<br/>

## Recipe features
Latest version of Discord.py running on a load balanced **Zerops Python** service.

<br/>

## Setting up Environment Variables

The steps mentioned here are to be followed after deploying the app and will guide you on how to obtain the two required environment variables to run your Discord.js Bot.

1. Go to the [Discord Application Portal](https://discord.com/developers/applications). Create an application if you do not have one already.

- Go to the Bot section (sidebar), reset the token, and copy the token. This will be used for `DISCORD_TOKEN`.

2. Head to your service. If you have full mode, check your sidebar and click on Environment Variables. On that page, you will see an "edit multiple secret variables in .env format" button. Click on it, paste your environment variable in the format shown below, and click on Update Secret Variables. You will then see a button to commit your changes.

```env
# Your Application ID copied from the Bot section.
DISCORD_TOKEN=MTIyNjQ3NDYwNjExODk2NTI3MA.GtSgOF.W7wLWibfGtP2tobLv_DsbFKdjlGmOwzxliTejI 
```

## Production vs. development
This recipe is ready for production as is, and will scale horizontally by adding more containers in case of high traffic surges. If you want to achieve the highest baseline reliability and resiliace, start with at least two containers (add `minContainers: 2` in recipe YAML in the `bot` service section, or change the minimum containers in "Automatic Scaling configuration" section of service detail).

<br/>

## Changes made over the default installation
If you want to modify your existing Discord.js bot to efficiently run on Zerops, there are no changes needed in the codebase on top of the standard installation, just add [zerops.yml](https://github.com/zeropsio/recipe-discord-py/blob/main/zerops.yml) to your repository.

<br/>
<br/>

Need help setting your project up? Join [Zerops Discord community](https://discord.com/invite/WDvCZ54).