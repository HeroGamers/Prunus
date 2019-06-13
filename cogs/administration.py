import asyncio
import discord
from discord import Embed
from discord.ext import commands
import os

class administration:
    def __init__(self,bot):
        self.bot = bot
        
        @bot.command()
        @commands.has_role("Administrative Perms")
        async def membersinrole(ctx, arg1):
            """Counts how many members are in a role"""
            memberCount = 0
            memberCountAll = len(ctx.guild.members)
            embed = discord.Embed(title="Tjekker medlemmer...", color=discord.Color.green(),
                    description="Tjekker %s medlemmer..." % (memberCountAll))
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed_message = await ctx.send(embed=embed)
            for member in ctx.guild.members:
                # Checking for bot roles
                roletocheck = int(arg1)
                role = discord.utils.get(ctx.guild.roles, id=roletocheck)
                if roletocheck in [y.id for y in member.roles]:
                    memberCount += 1
                    if memberCount == 10 or memberCount == 50 or memberCount == 100:
                        embed = discord.Embed(title="Tjekker medlemmer...", color=discord.Color.green(),
                            description="Fundet %s medlemmer i rollen %s 👌" % (memberCount, role.name))
                        await embed_message.edit(embed=embed)
                    else:
                        pass
                else:
                    pass
            embed = discord.Embed(title="Tjekket alle medlemmer!", color=discord.Color.green(),
                    description="Der er %s medlemmer i rollen %s 👌" % (memberCount, role.name))
            await embed_message.edit(embed=embed)

        @bot.command()
        @commands.has_role("Administrative Perms")
        async def removerolefromall(ctx, arg1):
            """Removes a role from all users"""
            channel = bot.get_channel(int(os.getenv('botlog')))
            memberCount = 0
            memberCountAll = len(ctx.guild.members)
            embed = discord.Embed(title="Fjerner rolle fra alle...", color=discord.Color.green(),
                    description="%s/%s medlemmer er blevet tjekket..." % (memberCount, memberCountAll))
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed_message = await ctx.send(embed=embed)
            for member in ctx.guild.members:
                # Removing role
                removerole = int(arg1)
                role = discord.utils.get(ctx.guild.roles, id=removerole)
                try:
                    await member.remove_roles(role)
                    await channel.send(f"**[Info]** Removed the {role.name} role from the member {member.name}")
                except Exception as e:
                    await ctx.send(f"Failed to remove the {role.name} role from the member {member.name}")
                    await channel.send(f"**[ERROR]** Failed to remove the {role.name} role from the member {member.name} - {e}")
                memberCount += 1
                if memberCount == 10 or memberCount == 50 or memberCount == 100:
                    embed = discord.Embed(title="Fjerner rolle fra alle...", color=discord.Color.green(),
                        description="%s/%s medlemmer er blevet tjekket 👌" % (memberCount, memberCountAll))
                    await embed_message.edit(embed=embed)
                else:
                    pass
            embed = discord.Embed(title="Fjernet rolle fra alle!", color=discord.Color.green(),
                    description="%s/%s medlemmer er blevet tjekket 👌" % (memberCount, memberCountAll))
            await embed_message.edit(embed=embed)

        @bot.command()
        @commands.has_role("Hero")
        async def updateroles(ctx):
            """Updates users roles"""
            channel = bot.get_channel(int(os.getenv('botlog')))
            memberCount = 0
            memberCountAll = len(ctx.guild.members)
            embed = discord.Embed(title="Opdaterer roller...", color=discord.Color.green(),
                    description="%s/%s medlemmer er blevet tjekket..." % (memberCount, memberCountAll))
            embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed_message = await ctx.send(embed=embed)
            for member in ctx.guild.members:
                # Checking for bot roles
                newrole = 519257824300236826
                rolecheck = [300676025006817282, 427511769158778883]
                role = discord.utils.get(ctx.guild.roles, id=newrole)
                for integer in rolecheck:
                    if (integer in [y.id for y in member.roles]):
                        if newrole in [y.id for y in member.roles]:
                            pass
                        else:
                            try:
                                await member.add_roles(role)
                                await channel.send(f"**[Info]** Added the {role.name} role to the member {member.name}")
                            except Exception as e:
                                await ctx.send(f"Failed to add the {role.name} role to the member {member.name}")
                                await channel.send(f"**[ERROR]** Failed to add the {role.name} role to the member {member.name} - {e}")
                    else:
                        pass
                # Checking for staff roles
                # Prison, Factions, Survival, Creative, Minigames
                newrole = 519253907151781916
                rolecheck = [380069922145042432, 365615127006806016, 365615114529013762, 365615418838351873, 365615310675378176]
                role = discord.utils.get(ctx.guild.roles, id=newrole)
                for integer in rolecheck:
                    if (integer in [y.id for y in member.roles]):
                        if newrole in [y.id for y in member.roles]:
                            pass
                        else:
                            try:
                                await member.add_roles(role)
                                await channel.send(f"**[Info]** Added the {role.name} role to the member {member.name}")
                            except Exception as e:
                                await ctx.send(f"Failed to add the {role.name} role to the member {member.name}")
                                await channel.send(f"**[ERROR]** Failed to add the {role.name} role to the member {member.name} - {e}")
                    else:
                        pass
                # Checking for special roles
                # Staff, Ex-Staff, Streamer, SteamMod, StreamGuest, Arkitekt, DoggyCrafter, Memelord, GM
                newrole = 519258641967218728
                rolecheck = [413441511439466509, 488786258835800077, 407264731192360962, 409409068076236801, 409489018166968347, 503241332173832223, 339390105288441857, 417068142796341248]
                role = discord.utils.get(ctx.guild.roles, id=newrole)
                for integer in rolecheck:
                    if (integer in [y.id for y in member.roles]):
                        if newrole in [y.id for y in member.roles]:
                            pass
                        else:
                            try:
                                await member.add_roles(role)
                                await channel.send(f"**[Info]** Added the {role.name} role to the member {member.name}")
                            except Exception as e:
                                await ctx.send(f"Failed to add the {role.name} role to the member {member.name}")
                                await channel.send(f"**[ERROR]** Failed to add the {role.name} role to the member {member.name} - {e}")
                    else:
                        pass
                # Checking for war roles
                # Rebel, Imperial, Neutral
                newrole = 519257488416047115
                rolecheck = [262385568783138817, 262385495252664321, 339435983458271233]
                role = discord.utils.get(ctx.guild.roles, id=newrole)
                for integer in rolecheck:
                    if (integer in [y.id for y in member.roles]):
                        if newrole in [y.id for y in member.roles]:
                            pass
                        else:
                            try:
                                await member.add_roles(role)
                                await channel.send(f"**[Info]** Added the {role.name} role to the member {member.name}")
                            except Exception as e:
                                await ctx.send(f"Failed to add the {role.name} role to the member {member.name}")
                                await channel.send(f"**[ERROR]** Failed to add the {role.name} role to the member {member.name} - {e}")
                    else:
                        pass
                # Checking for referral roles
                newrole = 519257183305728011
                rolecheck = [422860967727202314]
                role = discord.utils.get(ctx.guild.roles, id=newrole)
                for integer in rolecheck:
                    if (integer in [y.id for y in member.roles]):
                        if newrole in [y.id for y in member.roles]:
                            pass
                        else:
                            try:
                                await member.add_roles(role)
                                await channel.send(f"**[Info]** Added the {role.name} role to the member {member.name}")
                            except Exception as e:
                                await ctx.send(f"Failed to add the {role.name} role to the member {member.name}")
                                await channel.send(f"**[ERROR]** Failed to add the {role.name} role to the member {member.name} - {e}")
                    else:
                        pass
                # Checking for chat roles
                # TechTalk, Alpha, 18+, Roleplaying
                newrole = 519259311793373191
                rolecheck = [406137615184822282, 417043711499698178, 262386253264060416, 262386488749195275]
                role = discord.utils.get(ctx.guild.roles, id=newrole)
                for integer in rolecheck:
                    if (integer in [y.id for y in member.roles]):
                        if newrole in [y.id for y in member.roles]:
                            pass
                        else:
                            try:
                                await member.add_roles(role)
                                await channel.send(f"**[Info]** Added the {role.name} role to the member {member.name}")
                            except Exception as e:
                                await ctx.send(f"Failed to add the {role.name} role to the member {member.name}")
                                await channel.send(f"**[ERROR]** Failed to add the {role.name} role to the member {member.name} - {e}")
                    else:
                        pass
                # Checking for news roles
                newrole = 519570187213602825
                rolecheck = [382282906552500237]
                role = discord.utils.get(ctx.guild.roles, id=newrole)
                for integer in rolecheck:
                    if (integer in [y.id for y in member.roles]):
                        if newrole in [y.id for y in member.roles]:
                            pass
                        else:
                            try:
                                await member.add_roles(role)
                                await channel.send(f"**[Info]** Added the {role.name} role to the member {member.name}")
                            except Exception as e:
                                await ctx.send(f"Failed to add the {role.name} role to the member {member.name}")
                                await channel.send(f"**[ERROR]** Failed to add the {role.name} role to the member {member.name} - {e}")
                    else:
                        pass
                memberCount += 1
                if memberCount == 10 or memberCount == 50 or memberCount == 100:
                    embed = discord.Embed(title="Opdaterer roller...", color=discord.Color.green(),
                        description="%s/%s medlemmer er blevet tjekket 👌" % (memberCount, memberCountAll))
                    await embed_message.edit(embed=embed)
                else:
                    pass
            embed = discord.Embed(title="Opdateret alle roller!", color=discord.Color.green(),
                    description="%s/%s medlemmer er blevet tjekket 👌" % (memberCount, memberCountAll))
            await embed_message.edit(embed=embed)

        @bot.command()
        @commands.has_role("Administrative Perms")
        async def listroles(ctx):
            """Gives roles and id's"""
            roles = []
            for role in ctx.guild.roles:
                roles.append("%s - `%s`\n" % (role.name, role.id))
            joined_string = ' '.join([str(v) for v in roles])
            await ctx.send(joined_string)
            
                
            
def setup(bot):
    bot.add_cog(administration(bot))
