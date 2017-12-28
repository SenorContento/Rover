This is the beginning of an AI by Brandon Gomez (SenorContento) for himself! Designed for his Raspberry Pi 3 (Model B) running Raspian!

The links below are just different resources for Rover! Not all of them are useful, such as Pocket Edition Minecraft (as there is currently no support for pocket edition right now) and some of them are just for the test server, which is whitelisted as it is only for developers and friends to join. As I am currently the only developer of this project, that means that it is only for friends as of now.

# Links

* Website - [Rover's Site](https://rover.senorcontento.com/)
* Telegram - [@MrCsDigitalRoverBot](https://t.me/MrCsDigitalRoverBot)
* Telegram News Channel - [@RoverChannel](https://t.me/RoverChannel)
* Discord - [Rover#4549](https://discordapp.com/channels/@me/314885235495927808)
* Discord (Add to Server) - [Rover#4549](https://brandons.site/roverDiscord)
* Minecraft - [DigitalRover](https://namemc.com/profile/aac15086-9b8f-4fb6-bb33-ff27cae2d873)
* Minecraft (Pocket Edition) - [DigitalRover](https://account.xbox.com/en-us/Profile?gamerTag=DigitalRover)
* Minecraft Test Server - [Server](http://play.minecraft.senorcontento.com:25565/)
* Minecraft Test Server Site - [Website](https://minecraft.senorcontento.com/)
* Minecraft Test Server Status - [Status](https://mcserverstatus.com/viewserver/33931)

# Donate

If you happen across this project and want to help out, please donate to me. You can use a method such as Paypal, https://www.paypal.me/SenorContento, to donate, or if not, I have a Coinbase account to accept Bitcoins. Any donations will be appreciated and will be used to help fund the project any way it can (What I mean by that is I am a college student and my only paying job is working at a restaurant at my school. Any donations to ease the burden of paying for college and supporting me will make it so much easier to focus on my projects).

# Minecraft

I am going to be working on the project https://github.com/ammaraskar/pyCraft! I have a fork located at https://github.com/SenorContento/pyCraft! So, that means if you want to use the Minecraft module as this module will be set to work with my fork, then you need to copy the folder minecraft from the root of pyCraft to this project's root! Now, if you want to help with any of this project, you are more than welcome to!

Also, if you are worried about any licensing issues, I quoted the below text from https://www.apache.org/licenses/GPL-compatibility.html!

"Apache 2 software can therefore be included in GPLv3 projects, because the GPLv3 license accepts our software into GPLv3 works. However, GPLv3 software cannot be included in Apache projects. The licenses are incompatible in one direction only, and it is a result of ASF's licensing philosophy and the GPLv3 authors' interpretation of copyright law."

I also checked [Mojang's EULA](https://account.mojang.com/documents/minecraft_eula) and it appears there is nothing preventing me from creating the bot, so I should be good. After all, you still have to pay for a Minecraft account to join people's servers (as I am not giving you access to my account). It really is no different than using Forge except that this isn't Mojang's client being modified, this is just a brand new client all in itself (solely for the purpose of automated Minecraft much like the [ComputerCraft Mod](https://github.com/dan200/ComputerCraft), but both in vanilla (and maybe in conjunction with mods such as ComputerCraft).

I wanted to have [pyCraft](https://github.com/ammaraskar/pyCraft) as a submodule or subtree, but it turns out there is not simple way of pulling the subdirectory, minecraft, and moving it here automatically. Things are made worse because some of the imports in the project are hardcoded and so they break if minecraft is not in the root of Rover. Sadly, there is no simple solution on my end, but I may see about a way to fix it if I edit this project. If you do want to use pyCraft, just clone the repo and move the directory "minecraft" over to the root of Rover. The root should be the folder you found this README in.
