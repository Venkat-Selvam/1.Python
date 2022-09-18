class SubfieldsInAI():
    def Subfields():
        Field_Name=input("Enter Your Field name:")
        Course,Course1="AI", "Music"

        if(Field_Name==Course):
            print("Sub-fields in AI are:")
            print("Machine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
            domain="Machine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing"

        elif(Field_Name==Course1):
            print("Sub-fields in Music are:")
            print("Music Production\nMusic Direction\nComposer\nSound Engineer\nConductor\nMixing and Mastering\nDrumer")
            domain="Music Production\nMusic Direction\nComposer\nSound Engineer\nConductor\nMixing and Mastering\nDrumer"

        else:
            print("Please Check Your Field Name...")
            domain="Please Check Your Field Name..."
        return domain

