define e = Character("Eileen")
define lassiter = Character("Detective Lassiter")
define shawn = Character("Shawn")
define barry = Character("Detective Barry")
define allen = Character("Officer Allen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music

    play music "audio/Trial.mp3"

    scene bg interrogation_room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show shawn laidback at center: 
        zoom 0.5

    shawn "So when do I get my money?"

    hide shawn laidback

    show barry serious at center:
        zoom 0.5

    # These display lines of dialogue.

    barry "Money?"

    hide barry serious

    show shawn laidback at center: 
        zoom 0.5

    shawn "Yeah. The reward for solving your case."

    hide shawn laidback

    show barry serious at right:
        zoom 0.5
    show lassiter serious at left:
        zoom 0.5
    lassiter "Why don’t you let us ask the questions here?"

    hide barry serious
    hide lassiter serious

    show shawn laidback at center: 
        zoom 0.5

    shawn "Fine. Ask away."

    hide shawn laidback

    show lassiter serious at center:
        zoom 0.5

    lassiter "Where were you the night of the robbery?"

    hide lassiter serious

    show shawn laidback at center: 
        zoom 0.5

    shawn "{i}I was robbing a stereo shop.{/i}"
    shawn "Hah, hah. Kidding. But seriously, how is this even a\nconversation? I gave you the guy!"

    hide shawn laidback

    show lassiter serious at center:
        zoom 0.5
    lassiter "He had a partner. Someone on the inside tipped him\noff. That’s what we’re betting on."

    hide lassiter serious

    show shawn laidback at center: 
        zoom 0.5
    shawn "Inside of what? Look, I’ve called in dozens of tips \nbefore.Check it out."

    hide shawn laidback

    show lassiter serious at center:
        zoom 0.5
    lassiter "Oh, I did. Like how you’ve never held a job \nlonger than six months. Or that little car-stealing\nincident back in high school."

    hide lassiter serious

    show shawn laidback at center: 
        zoom 0.5
    shawn "It was borrowed! To impress a girl.\nMy dad arrested me to\n'teach me a lesson.'\nDid I learn anything? Yeah—I hated him after that."

    hide shawn laidback

    show lassiter serious at center:
        zoom 0.5
    lassiter "And yet somehow, you solved all these crimes by\nwatching TV interviews?"

    hide lassiter serious

    show shawn laidback at center: 
        zoom 0.5
    shawn "Can’t you?"

    hide shawn laidback

    show lassiter serious at center:
        zoom 0.5
    lassiter "Don’t you trivialize police work."

    hide lassiter serious

    show shawn laidback at center: 
        zoom 0.5
    shawn "You’re doing a bang-up job at that yourself.\nYou can’t keep me here. I know my rights."

    # Shawn tries to leave.
    hide shawn laidback
    show shawn laidback at center:
        zoom 0.5
    shawn "(stands and heads for the door)"

    # Officer blocks his exit.
    hide shawn laidback
    show lassiter serious at center:
        zoom 0.5
    lassiter "Good. Then you know you have the right to remain\nsilent."

    hide lassiter serious

    show shawn laidback at center:
        zoom 0.5

    shawn "Are you serious?"

    hide shawn laidback

    show lassiter serious at left:
        zoom 0.5
    show barry serious at right:
        zoom 0.5
    barry "Just give us a reason, Mr. Spencer. How did you\nreally get this information?"

    lassiter "No. It’s too late for excuses. Officer Allen, book him."

    hide lassiter serious
    hide barry serious

    show allen neutral at center:
        zoom 0.5
    allen "Yes, Detective." 

    # Shawn notices Allen's laidback accessories.
    hide allen neutral
    show shawn laidback at center:
        zoom 0.5
    shawn "(spots Allen's crystal pendant and earrings) Hmm..."

label decision:
    # Player choice: Stick with the truth or pretend to be psychic.
    menu:
        "Stick with the truth":
            jump truth_path
        "Pretend to be psychic":
            jump psychic_path

label truth_path:
    show shawn laidback at center:
        zoom 0.5
    shawn "Look, I’m not lying! I just... watch people closely!"
    
    hide shawn laidback
    show lassiter serious at center:
        zoom 0.5
    lassiter "Save it for the holding cell."
    hide lassiter

    stop music

    show bg cell
    with fade
    
    show bg black
    with fade

    play music "audio/Shawn_screaming.mp3"
    shawn ""
    stop music

    play music "audio/Trial.mp3"
    show bg interrogation_room
    with fade

    show lassiter serious at center:
        zoom 0.5
    lassiter "Now, do you want to try that again?"
    hide lassiter
    
    jump decision

label psychic_path:
    show shawn laidback at center:
        zoom 0.5
    shawn "Wait! Okay, fine—you caught me. I’m a psychic."

    hide shawn laidback
    show allen neutral at right:
        zoom 0.5
    allen "(drops cuffs) What?"

    hide allen neutral
    show shawn laidback at center:
        zoom 0.5
    shawn "(puts hands up) Your grandma would be so proud."

    hide shawn laidback
    show allen neutral at right:
        zoom 0.5
    allen "You spoke to her?"

    hide allen neutral
    show shawn laidback at center:
        zoom 0.5
    shawn "I did. She's... safe, comfortable. She wants you to \nstop spending all your money on those charlatans."

    hide shawn laidback
    show allen neutral at right:
        zoom 0.5
    allen "(cups face) The palm readers."

    hide allen neutral
    show shawn laidback at center:
        zoom 0.5
    shawn "Exactly. Now, about that vandalism case—check\ndetention room two. The evidence is in the vandal's\nleft shoe."

    hide shawn laidback
    show lassiter serious at center:
        zoom 0.5
    lassiter "We’ll see about that. Let’s go."

    hide lassiter serious

    return