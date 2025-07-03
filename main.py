
import discord
from discord.ext import  commands
import logging
from dotenv import load_dotenv
import os
import random

load_dotenv()
token=os.getenv("DISCORD_TOKEN")

handler=logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents=discord.Intents.default()
intents.message_content=True
intents.members=True
intents.presences=True
intents.emojis=True

bot=commands.Bot(command_prefix='*',intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower()

    # Define word categories
    profanity_words = [
        "fuck", "shit", "bitch", "bastard", "dick", "cunt", "asshole", "crap", "damn", "bollocks",
        "prick", "motherfucker", "retard", "bloody", "slut", "twat", "wanker", "fucker"
    ]
    sexual_words = [
        "sex", "sexy", "porn", "nude", "nudes", "xxx", "horny", "naked", "boobs", "vagina", "penis",
        "pussy", "cum", "milf", "blowjob", "bj", "handjob", "69", "threesome", "anal", "fetish",
        "deepthroat", "tits", "moan", "orgasm"
    ]
    hate_speech_words = [
        "nigger", "nigga", "chink", "spic", "fag", "faggot", "tranny", "kike", "gook", "cripple",
        "coon", "homo", "dyke", "towelhead", "sandnigger", "nazis", "hitler", "heil hitler"
    ]
    self_harm_words = [
        "kill myself", "kys", "suicide", "hang myself", "cut myself", "die alone", "end it all",
        "overdose", "slit my wrist", "hate myself"
    ]
    drug_words = [
        "weed", "coke", "cocaine", "heroin", "meth", "lsd", "mdma", "acid", "ecstasy", "marijuana",
        "shrooms", "xanax", "adderall"
    ]

    # Check and handle
    def contains_any(msg, words):
        return any(word in msg for word in words)

    if contains_any(msg, profanity_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} ⚠️ Watch your language! Profanity is not allowed.")
    elif contains_any(msg, sexual_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} 🔞 Please keep sexual content out of this server.")
    elif contains_any(msg, hate_speech_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} 🚫 Hate speech or slurs are strictly forbidden here.")
    elif contains_any(msg, self_harm_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} 💬 We're here to support you. Please reach out to someone.")
    elif contains_any(msg, drug_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} 🚭 Drug-related discussions are not appropriate here.")

    await bot.process_commands(message)

@bot.event
async def on_member_update(before, after):
    # Define the role name or ID that triggers a ban
    auto_ban_role_name = "Banned"

    # Get the new roles added
    new_roles = set(after.roles) - set(before.roles)

    for role in new_roles:
        if role.name == auto_ban_role_name:
            try:
                await after.ban(reason="Auto-ban role assigned.")
                print(f"Banned {after.name} for having role '{role.name}'")
                break
            except discord.Forbidden:
                print(f"Missing permissions to ban {after.name}")
            except Exception as e:
                print(f"Error banning {after.name}: {e}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"hey!! {ctx.author.mention}")

@bot.command()
async def hey(ctx):
    greetings = [
        "Hey hey hey! 👋", "What's up! 😄", "Yo! ✌️", "Hola amigo! 🌮", "Howdy partner! 🤠",
        "Wassup! 🤙", "Oh hi there! 👀", "A wild user appeared! 🐾", "Hewwo~ 🐱", "Greetings, Earthling! 👽"
    ]
    await ctx.send(f"{random.choice(greetings)} {ctx.author.mention}")

@bot.command()
async def hug(ctx, member: discord.Member = None):
    hugs = [
        "gives a big warm hug 🤗", "squeezes tightly 💞", "wraps you in a blanket burrito 🌯",
        "sends virtual cuddles 🧸", "hugs like a teddy bear 🐻", "hugs with all the love 💓",
        "gives a super-soft squish 🫂", "teleports a hug from the void 🌌", "throws you a fuzzy hug ball 🧶",
        "launches a surprise hug attack 🚀🤗"
    ]
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"{ctx.author.mention} {random.choice(hugs)} to {target}")

@bot.command()
async def slap(ctx, member: discord.Member = None):
    slaps = [
        "slaps with a giant tuna 🐟", "throws a rubber chicken at them 🐔", "gently slaps with a feather 🪶",
        "smacks with a coding textbook 📚", "slaps using raw spaghetti 🍝", "smacks with a sock filled with glitter 🧦✨",
        "slaps with a pancake stack 🥞", "hits with a squeaky toy 🐶", "bonks with a plushie hammer 🔨",
        "yeets a pillow to their face 🛏️"
    ]
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"{ctx.author.mention} {random.choice(slaps)} at {target}")

@bot.command()
async def roast(ctx, member: discord.Member = None):
    roasts = [
        "You're as bright as a black hole.", "Your secrets are always safe with me. I never even listen.",
        "You have something on your chin... no, the third one down.", "You're the reason shampoo has instructions.",
        "You bring everyone so much joy… when you leave the room.", "You're not stupid; you just have bad luck thinking.",
        "If I had a dollar for every smart thing you said, I’d be broke.", "You have something on your face: stupidity.",
        "You’re like a cloud. When you disappear, it’s a beautiful day.", "I’d agree with you but then we’d both be wrong."
    ]
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"{target}, {random.choice(roasts)} 🔥")

@bot.command()
async def compliment(ctx, member: discord.Member = None):
    compliments = [
        "You're like sunshine on a rainy day ☀️", "You make people smile effortlessly 😁",
        "You have a heart of gold 💛", "You're more helpful than you know 👏",
        "You're a walking ray of happiness 🌟", "You inspire others to be better 💫",
        "You’re the human version of a cupcake 🧁", "You glow brighter than the stars 🌌",
        "You have impeccable vibes ✨", "You're cooler than the other side of the pillow 🧊"
    ]
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"{target}, {random.choice(compliments)} 💕")

@bot.command()
async def vibe(ctx):
    vibes = [
        "🎶 vibing with lo-fi beats", "😎 chilling in cool mode", "🌊 surfing the vibe wave",
        "🍵 sipping tea and watching clouds", "💃 dancing like no one's watching",
        "✨ floating through a calm cosmos", "🎧 lost in the rhythm", "☁️ soft vibes all around",
        "🎸 strumming the strings of peace", "🕺 dropping funky moves!"
    ]
    await ctx.send(f"{ctx.author.mention} is {random.choice(vibes)}")

@bot.command()
async def flip(ctx):
    result = random.choice(["Heads 🪙", "Tails 🪙", "It landed on its edge!? 😲"])
    await ctx.send(f"{ctx.author.mention} flipped a coin and got: **{result}**")

@bot.command()
async def roll(ctx, sides: int = 6):
    if sides < 2:
        await ctx.send("🎲 Dice must have at least 2 sides, silly.")
    else:
        result = random.randint(1, sides)
        await ctx.send(f"{ctx.author.mention} rolled a {result} on a {sides}-sided die 🎲")

@bot.command()
async def dm(ctx, member: discord.Member, *, message):
    try:
        await member.send(f"📩 You received a message from {ctx.author.mention}: {message}")
        await ctx.send(f"✅ DM sent to {member.mention}!")
    except discord.Forbidden:
        await ctx.send("❌ I couldn't DM that user. They might have DMs disabled.")

@bot.command()
async def reply(ctx):
    embed = discord.Embed(
        title="📩 Reply Received!",
        description="Thanks for your message! Here's a fancy reply just for you ✨",
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
    embed.timestamp = ctx.message.created_at

    await ctx.reply(f"{ctx.author.mention}, here's your special reply!", embed=embed)




bot.run(token,log_handler=handler,log_level=logging.DEBUG)