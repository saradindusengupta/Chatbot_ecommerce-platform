import aiml
bot=aiml.Kernel()


bot.learn("Computers.aiml")
bot.learn("Knowledge.aiml")
bot.learn("learn.aiml")
while True:
    print bot.respond(raw_input("=> "))


