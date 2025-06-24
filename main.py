import os
import logging
from flask import Flask, jsonify

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "gossip-girl-secret-key")

# Complete episode recaps dictionary for all 121 episodes
episode_recaps = {
    # Season 1 (18 episodes)
    (1, 1): {"season": 1, "episode": 1, "title": "Pilot", "recap": "Serena van der Woodsen returns to the Upper East Side from boarding school, causing a stir among her former friends. Blair Waldorf feels threatened by Serena's return, especially regarding her relationship with Nate Archibald. Dan Humphrey becomes smitten with Serena after a chance encounter."},
    (1, 2): {"season": 1, "episode": 2, "title": "The Wild Brunch", "recap": "Serena and Blair's friendship remains strained. A brunch at the Palace Hotel becomes the setting for more Upper East Side drama. Dan struggles with his feelings for Serena while dealing with class differences."},
    (1, 3): {"season": 1, "episode": 3, "title": "Poison Ivy", "recap": "College visits begin with Ivy League schools courting the privileged students. Serena visits Brown University but finds herself distracted by her complicated past. Blair obsesses over getting into Yale."},
    (1, 4): {"season": 1, "episode": 4, "title": "Bad News Blair", "recap": "Blair's world comes crashing down when she discovers her father is having an affair and her parents are getting divorced. She handles the news poorly, lashing out at those around her."},
    (1, 5): {"season": 1, "episode": 5, "title": "Dare Devil", "recap": "A charity event becomes the backdrop for relationship drama. Serena finds herself torn between Dan and Nate, while Blair continues to struggle with her parents' divorce."},
    (1, 6): {"season": 1, "episode": 6, "title": "The Handmaiden's Tale", "recap": "Blair's minions turn against her when she can't get them into the exclusive social events they desire. Serena helps Dan get into a VIP party, causing friction with Blair."},
    (1, 7): {"season": 1, "episode": 7, "title": "Victor/Victrola", "recap": "Chuck opens a club and Blair decides to perform there to win his attention. The episode explores Blair's desperation and Chuck's manipulative nature as their relationship begins to develop."},
    (1, 8): {"season": 1, "episode": 8, "title": "Seventeen Candles", "recap": "Blair's 17th birthday party becomes a disaster when her friends abandon her for Serena's spontaneous gathering. The episode highlights the shifting social dynamics among the group."},
    (1, 9): {"season": 1, "episode": 9, "title": "Blair Waldorf Must Pie!", "recap": "Thanksgiving brings family drama as Blair tries to impress her mother's new boyfriend. Serena deals with her own family issues while Dan learns about the complexities of upper-class relationships."},
    (1, 10): {"season": 1, "episode": 10, "title": "Hi, Society", "recap": "The annual Cotillion approaches and Blair is determined to be Queen. Serena reluctantly participates while dealing with pressure from her grandmother. Chuck and Nate's friendship is tested."},
    (1, 11): {"season": 1, "episode": 11, "title": "Roman Holiday", "recap": "Blair wins the Cotillion but her victory feels hollow. Chuck and Blair share their first real moment together. Serena's family secrets begin to surface, threatening her relationship with Dan."},
    (1, 12): {"season": 1, "episode": 12, "title": "School Lies", "recap": "Serena's past catches up with her when someone from her boarding school days threatens to expose her secrets. Blair struggles with her feelings for Chuck while trying to maintain her relationship with Nate."},
    (1, 13): {"season": 1, "episode": 13, "title": "A Thin Line Between Chuck and Nate", "recap": "Chuck and Nate's friendship reaches a breaking point over Blair. Serena faces consequences for her past actions, and Dan must decide if he can handle the truth about her history."},
    (1, 14): {"season": 1, "episode": 14, "title": "The Blair Bitch Project", "recap": "Blair orchestrates a plan to humiliate Georgina Sparks, who has returned to threaten Serena. The episode reveals more about Serena's dark past and the lengths Blair will go to protect her friend."},
    (1, 15): {"season": 1, "episode": 15, "title": "Desperately Seeking Serena", "recap": "Serena goes missing after Georgina's latest scheme, leaving everyone worried. Blair and Dan must work together to find her, while Chuck deals with his own family drama."},
    (1, 16): {"season": 1, "episode": 16, "title": "All About My Brother", "recap": "Family secrets explode when Eric's suicide attempt is revealed. Serena's family must confront their issues while Blair supports her friend through the crisis."},
    (1, 17): {"season": 1, "episode": 17, "title": "Woman on the Verge", "recap": "Serena's mother Lily faces her own crisis while Serena tries to help her family heal. Blair and Chuck's relationship continues to develop in unexpected ways."},
    (1, 18): {"season": 1, "episode": 18, "title": "Much 'I Do' About Nothing", "recap": "Season finale brings multiple revelations as family secrets are exposed and relationships are forever changed. Serena and Dan's relationship faces its biggest test yet."},

    # Season 2 (25 episodes)
    (2, 1): {"season": 2, "episode": 1, "title": "Summer Kind of Wonderful", "recap": "Summer in the Hamptons brings new complications. Serena is in Europe while Blair rules the Hamptons social scene. Dan works as a busboy, creating tension with his privileged peers."},
    (2, 2): {"season": 2, "episode": 2, "title": "Never Been Marcused", "recap": "Blair and Serena's friendship faces new challenges as they compete for social dominance. A charity auction becomes the setting for power plays and romantic maneuvering."},
    (2, 3): {"season": 2, "episode": 3, "title": "The Dark Night", "recap": "Halloween brings out everyone's dark side as secrets are revealed and relationships are tested. Costume parties provide cover for deception and manipulation."},
    (2, 4): {"season": 2, "episode": 4, "title": "The Ex-Files", "recap": "Past relationships complicate present ones as old flames return. Serena and Dan face challenges from their romantic histories while Blair deals with her own complicated feelings."},
    (2, 5): {"season": 2, "episode": 5, "title": "The Serena Also Rises", "recap": "Serena's rising popularity in the fashion world threatens Blair's position as queen bee. Professional jealousy strains their friendship as both girls compete for the spotlight."},
    (2, 6): {"season": 2, "episode": 6, "title": "New Haven Can Wait", "recap": "College interviews create pressure and competition among the seniors. Blair's Yale dreams face obstacles while other characters confront their own academic futures."},
    (2, 7): {"season": 2, "episode": 7, "title": "Chuck in Real Life", "recap": "Chuck tries to prove he's changed by pursuing a normal relationship. His attempts at redemption are complicated by his past behavior and others' skepticism about his transformation."},
    (2, 8): {"season": 2, "episode": 8, "title": "Pret-a-Poor-J", "recap": "Jenny's fashion ambitions lead her into the competitive world of high-end design. She faces challenges that test her values and her relationships with family and friends."},
    (2, 9): {"season": 2, "episode": 9, "title": "There Might be Blood", "recap": "Thanksgiving dinner becomes a battlefield when family tensions explode. Multiple generations clash over secrets, loyalty, and the cost of keeping up appearances."},
    (2, 10): {"season": 2, "episode": 10, "title": "Bonfire of the Vanity", "recap": "A charity benefit becomes the setting for major revelations and confrontations. Past mistakes come back to haunt several characters as the truth finally comes to light."},
    (2, 11): {"season": 2, "episode": 11, "title": "The Magnificent Archibalds", "recap": "Nate's family faces a major scandal that threatens their social standing. The episode explores themes of loyalty, money, and the price of maintaining Upper East Side status."},
    (2, 12): {"season": 2, "episode": 12, "title": "It's a Wonderful Lie", "recap": "Christmas brings both joy and heartbreak as characters reflect on the year's events. Secrets are revealed and relationships are tested during the holiday season."},
    (2, 13): {"season": 2, "episode": 13, "title": "O Brother, Where Bart Thou?", "recap": "Chuck faces devastating loss when his father dies in a car accident. The tragedy forces him to confront his relationships and his future as he inherits the Bass empire."},
    (2, 14): {"season": 2, "episode": 14, "title": "In the Realm of the Basses", "recap": "Chuck struggles with grief and responsibility as he takes over his father's business. Blair tries to support him while dealing with her own family issues."},
    (2, 15): {"season": 2, "episode": 15, "title": "Gone with the Will", "recap": "Bart Bass's will reading brings unexpected revelations and new conflicts. Chuck discovers shocking truths about his father while fighting for his inheritance."},
    (2, 16): {"season": 2, "episode": 16, "title": "You've Got Yale!", "recap": "College acceptances and rejections create drama among the seniors. Blair's Yale dreams hang in the balance while others face their own academic disappointments."},
    (2, 17): {"season": 2, "episode": 17, "title": "Carnal Knowledge", "recap": "Romantic entanglements become more complicated as characters cross lines and break boundaries. Past relationships influence present decisions in unexpected ways."},
    (2, 18): {"season": 2, "episode": 18, "title": "The Age of Dissonance", "recap": "Generational conflicts come to a head as parents and children clash over values and expectations. The younger generation rebels against traditional Upper East Side conventions."},
    (2, 19): {"season": 2, "episode": 19, "title": "The Grandfather", "recap": "Chuck's paternal grandfather arrives, bringing new complications to the Bass family dynamics. Old rivalries and new alliances form as family secrets are revealed."},
    (2, 20): {"season": 2, "episode": 20, "title": "Remains of the J", "recap": "Jenny's transformation reaches a critical point as she becomes more like the elite she once criticized. Her family worries about losing the girl they once knew."},
    (2, 21): {"season": 2, "episode": 21, "title": "Seder Anything", "recap": "A Passover celebration becomes the setting for family drama and romantic revelations. Religious traditions clash with modern values as characters confront their beliefs."},
    (2, 22): {"season": 2, "episode": 22, "title": "Southern Gentlemen Prefer Blondes", "recap": "A trip to the South introduces new characters and complications. Regional differences highlight the cultural divides that exist even within privileged society."},
    (2, 23): {"season": 2, "episode": 23, "title": "The Wrath of Con", "recap": "A elaborate con game threatens to destroy relationships and reputations. Trust becomes a luxury as characters question everyone's motives and loyalty."},
    (2, 24): {"season": 2, "episode": 24, "title": "Valley Girls", "recap": "A flashback episode reveals Lily's wild past in Los Angeles. The episode explores how the previous generation's choices influenced their children's current situations."},
    (2, 25): {"season": 2, "episode": 25, "title": "The Goodbye Gossip Girl", "recap": "Season finale brings major changes as Gossip Girl's identity is nearly revealed. Graduation approaches and relationships reach crucial turning points that will define the future."},

    # Season 3 (22 episodes)
    (3, 1): {"season": 3, "episode": 1, "title": "Reversals of Fortune", "recap": "Senior year begins with major changes. Chuck and Blair's relationship evolves while Serena faces new challenges. College applications loom large over everyone's decisions."},
    (3, 2): {"season": 3, "episode": 2, "title": "The Freshmen", "recap": "NYU orientation brings new challenges and opportunities. Dan embraces college life while trying to maintain his relationship with Serena. Blair struggles with not being the automatic queen bee."},
    (3, 3): {"season": 3, "episode": 3, "title": "The Lost Boy", "recap": "Chuck's emotional walls begin to crumble as he opens up to Blair. Meanwhile, Dan and Serena navigate the challenges of being in different places in their lives."},
    (3, 4): {"season": 3, "episode": 4, "title": "Dan de Fleurette", "recap": "Dan's attempt to fit into Serena's world leads to unexpected consequences. Blair helps Chuck deal with his emotional vulnerabilities while protecting their relationship."},
    (3, 5): {"season": 3, "episode": 5, "title": "Rufus Getting Married", "recap": "Rufus and Lily's wedding planning brings families together and creates new tensions. Past relationships complicate present happiness as secrets threaten the celebration."},
    (3, 6): {"season": 3, "episode": 6, "title": "Enough About Eve", "recap": "A new student threatens Blair's position at NYU. Competition and jealousy drive Blair to extreme measures as she fights to maintain her social standing."},
    (3, 7): {"season": 3, "episode": 7, "title": "How to Succeed in Bassness", "recap": "Chuck ventures into the music industry while dealing with his complicated relationship with Blair. Business and pleasure mix in dangerous ways."},
    (3, 8): {"season": 3, "episode": 8, "title": "The Grandfather: Part II", "recap": "Chuck's relationship with his grandfather becomes more complex as family loyalty is tested. Past grievances influence present decisions in the Bass family."},
    (3, 9): {"season": 3, "episode": 9, "title": "They Shoot Humphreys, Don't They?", "recap": "A charity event becomes the setting for romantic complications and social maneuvering. Dan finds himself caught between different worlds and conflicting loyalties."},
    (3, 10): {"season": 3, "episode": 10, "title": "The Last Days of Disco Stick", "recap": "A night out at a club leads to unexpected encounters and revelations. The episode explores themes of identity and authenticity in the social media age."},
    (3, 11): {"season": 3, "episode": 11, "title": "The Treasure of Serena Madre", "recap": "Serena's family secrets surface, threatening her relationship with Dan. Mother-daughter dynamics become complicated as past mistakes influence present relationships."},
    (3, 12): {"season": 3, "episode": 12, "title": "The Debarted", "recap": "A memorial service brings together past and present as characters reflect on loss and legacy. Grief affects everyone differently, revealing hidden strengths and vulnerabilities."},
    (3, 13): {"season": 3, "episode": 13, "title": "The Hurt Locket", "recap": "Chuck and Blair's relationship faces its biggest test yet when trust is broken. The episode explores whether love can overcome betrayal and past mistakes."},
    (3, 14): {"season": 3, "episode": 14, "title": "The Lady Vanished", "recap": "Blair disappears, leaving everyone searching for answers. Her absence forces the group to confront their relationships and priorities without their queen bee."},
    (3, 15): {"season": 3, "episode": 15, "title": "The Sixteen Year Old Virgin", "recap": "Jenny's coming-of-age story takes a dramatic turn as she makes important decisions about her future. Family relationships are tested as she asserts her independence."},
    (3, 16): {"season": 3, "episode": 16, "title": "The Empire Strikes Jack", "recap": "Chuck's uncle Jack returns, bringing trouble and testing Chuck's resolve. Family loyalty and business interests collide in dangerous ways."},
    (3, 17): {"season": 3, "episode": 17, "title": "Inglourious Bassterds", "recap": "Chuck plans his revenge against Jack while dealing with the consequences of his choices. The episode explores themes of justice, revenge, and redemption."},
    (3, 18): {"season": 3, "episode": 18, "title": "The Unblairable Lightness of Being", "recap": "Blair's identity crisis reaches a peak as she questions everything about her life. The episode examines what happens when someone loses their sense of self."},
    (3, 19): {"season": 3, "episode": 19, "title": "Dr. Estrangeloved", "recap": "Professional therapy becomes personal as characters confront their psychological issues. The episode explores mental health and the stigma surrounding seeking help."},
    (3, 20): {"season": 3, "episode": 20, "title": "It's a Dad, Dad, Dad, Dad World", "recap": "Father figures play important roles as characters deal with daddy issues and paternal relationships. The episode explores how parental relationships shape identity."},
    (3, 21): {"season": 3, "episode": 21, "title": "Ex-Husbands and Wives", "recap": "Past marriages and relationships complicate present romances. The adult generation's romantic history influences their children's understanding of love and commitment."},
    (3, 22): {"season": 3, "episode": 22, "title": "Last Tango, Then Paris", "recap": "Season finale takes the characters to Paris where major decisions are made about relationships and futures. The episode sets up significant changes for the next season."},

    # Season 4 (22 episodes)
    (4, 1): {"season": 4, "episode": 1, "title": "Belles de Jour", "recap": "Summer in Paris changes Serena as she tries to reinvent herself. Blair also spends time in Paris, leading to unexpected encounters and new relationships."},
    (4, 2): {"season": 4, "episode": 2, "title": "Double Identity", "recap": "Identity crises abound as characters struggle with who they are versus who they want to be. Serena returns from Paris with secrets while Blair faces new challenges."},
    (4, 3): {"season": 4, "episode": 3, "title": "The Undergraduates", "recap": "College life brings new pressures and opportunities. Dan, Blair, Serena, and Vanessa navigate the academic and social challenges of university while maintaining their complicated relationships."},
    (4, 4): {"season": 4, "episode": 4, "title": "Touch of Eva", "recap": "A mysterious new character enters the scene, bringing complications to existing relationships. Trust becomes an issue as characters question motives and hidden agendas."},
    (4, 5): {"season": 4, "episode": 5, "title": "Goodbye, Columbia", "recap": "College plans change dramatically for several characters. Academic and personal setbacks force everyone to reconsider their futures and what they really want from life."},
    (4, 6): {"season": 4, "episode": 6, "title": "Easy J", "recap": "Jenny's transformation continues as she becomes more involved with the elite social scene. Her family worries about losing touch with their values and their daughter."},
    (4, 7): {"season": 4, "episode": 7, "title": "War at the Roses", "recap": "A fashion show becomes a battlefield as Blair and Jenny compete for dominance. Professional rivalries become personal as ambition threatens family relationships."},
    (4, 8): {"season": 4, "episode": 8, "title": "Juliet Doesn't Live Here Anymore", "recap": "A dangerous new enemy targets Serena with elaborate schemes. Trust and friendship are tested as the group faces an external threat that brings them together."},
    (4, 9): {"season": 4, "episode": 9, "title": "The Witches of Bushwick", "recap": "Halloween brings supernatural themes as characters face their darkest fears. Costumes and masks provide cover for revealing true feelings and hidden motivations."},
    (4, 10): {"season": 4, "episode": 10, "title": "Gaslight", "recap": "Psychological manipulation reaches dangerous levels as one character's sanity is questioned. The episode explores themes of mental health and the power of gaslighting."},
    (4, 11): {"season": 4, "episode": 11, "title": "The Townie", "recap": "An outsider's perspective challenges the group's insular world. Class differences and cultural divides become apparent as new relationships form across social boundaries."},
    (4, 12): {"season": 4, "episode": 12, "title": "The Kids Are Not All Right", "recap": "Generational conflicts intensify as parents and children clash over values and expectations. The younger generation pushes back against traditional constraints and expectations."},
    (4, 13): {"season": 4, "episode": 13, "title": "Damien Darko", "recap": "A mysterious new character brings danger and excitement to the Upper East Side. Risk-taking behavior escalates as characters seek thrills and escape from their problems."},
    (4, 14): {"season": 4, "episode": 14, "title": "Panic Roommate", "recap": "Living situations become complicated as characters navigate roommate relationships and personal space. Privacy and intimacy become precious commodities in their interconnected world."},
    (4, 15): {"season": 4, "episode": 15, "title": "It-Girl Happened One Night", "recap": "A single night changes everything as characters make decisions that will have lasting consequences. The episode explores how one moment can alter the course of multiple lives."},
    (4, 16): {"season": 4, "episode": 16, "title": "While You Weren't Sleeping", "recap": "Sleep deprivation and stress take their toll as characters face mounting pressures. The episode examines how exhaustion affects judgment and relationships."},
    (4, 17): {"season": 4, "episode": 17, "title": "Empire of the Son", "recap": "Chuck faces challenges to his business empire while dealing with personal relationships. Power struggles and family dynamics complicate his path to success."},
    (4, 18): {"season": 4, "episode": 18, "title": "The Kids Stay in the Picture", "recap": "Photography and image-making become central themes as characters confront how they're perceived versus who they really are. Appearances versus reality take center stage."},
    (4, 19): {"season": 4, "episode": 19, "title": "Petty in Pink", "recap": "A charity luncheon becomes the setting for petty rivalries and social maneuvering. Small conflicts escalate into major confrontations as pride and ego take over."},
    (4, 20): {"season": 4, "episode": 20, "title": "The Princesses and the Frog", "recap": "Fairy tale themes contrast with harsh realities as characters' dreams meet real-world obstacles. The episode explores the gap between fantasy and reality in relationships."},
    (4, 21): {"season": 4, "episode": 21, "title": "Shattered Bass", "recap": "Chuck's world falls apart as personal and professional crises converge. The episode examines how people rebuild after losing everything they thought mattered."},
    (4, 22): {"season": 4, "episode": 22, "title": "The Wrong Goodbye", "recap": "Season finale brings major revelations about Gossip Girl's identity and sets up dramatic changes. Characters face life-altering decisions about their futures and relationships."},

    # Season 5 (24 episodes)
    (5, 1): {"season": 5, "episode": 1, "title": "Yes, Then Zero", "recap": "Post-graduation life begins as characters navigate new adult responsibilities. The transition from high school to real world proves more challenging than expected."},
    (5, 2): {"season": 5, "episode": 2, "title": "Beauty and the Feast", "recap": "Professional ambitions clash with personal relationships as characters pursue their career goals. Success comes at a cost as work-life balance becomes impossible to maintain."},
    (5, 3): {"season": 5, "episode": 3, "title": "The Jewel of Denial", "recap": "Denial becomes a coping mechanism as characters refuse to face difficult truths. The episode explores how avoiding reality only makes problems worse."},
    (5, 4): {"season": 5, "episode": 4, "title": "Memoirs of an Invisible Dan", "recap": "Dan's writing career takes off but at the cost of his relationships. The episode examines the ethics of using real people as inspiration for fiction."},
    (5, 5): {"season": 5, "episode": 5, "title": "The Fasting and the Furious", "recap": "Religious observance and spiritual seeking become important themes. Characters explore faith and tradition while questioning their beliefs and values."},
    (5, 6): {"season": 5, "episode": 6, "title": "I Am Number Nine", "recap": "Numbers and superstitions play a role as characters face important decisions. The episode explores how people create meaning and seek signs in uncertain times."},
    (5, 7): {"season": 5, "episode": 7, "title": "The Big Sleep No More", "recap": "Sleep and dreams become metaphors for escape and avoidance. Characters struggle with insomnia and nightmares as stress takes its toll on their mental health."},
    (5, 8): {"season": 5, "episode": 8, "title": "All the Pretty Sources", "recap": "Journalism and media ethics become central as characters deal with the power and responsibility of information. Truth becomes a commodity in the digital age."},
    (5, 9): {"season": 5, "episode": 9, "title": "Shiny Happy People", "recap": "Forced happiness and positive thinking mask deeper problems. The episode explores how social pressure to appear successful can hide genuine struggles."},
    (5, 10): {"season": 5, "episode": 10, "title": "Riding in Town Cars with Boys", "recap": "Transportation and mobility become metaphors for freedom and escape. Characters use travel and movement to avoid dealing with their problems."},
    (5, 11): {"season": 5, "episode": 11, "title": "The End of the Affair?", "recap": "Extramarital relationships and infidelity complicate family dynamics. The episode explores how affairs affect not just couples but entire social networks."},
    (5, 12): {"season": 5, "episode": 12, "title": "Father and the Bride", "recap": "Wedding planning brings out family tensions and hidden resentments. The episode examines how major life events can either unite or divide families."},
    (5, 13): {"season": 5, "episode": 13, "title": "G.G.", "recap": "Gossip Girl's influence reaches new heights as social media becomes more powerful. The episode explores the dark side of online culture and cyberbullying."},
    (5, 14): {"season": 5, "episode": 14, "title": "The Backup Dan", "recap": "Backup plans and second choices become important themes. Characters realize that sometimes the alternative path leads to unexpected happiness."},
    (5, 15): {"season": 5, "episode": 15, "title": "Crazy, Cupid, Love", "recap": "Valentine's Day brings romantic complications and unrequited love. The episode explores different types of love and how they affect relationships."},
    (5, 16): {"season": 5, "episode": 16, "title": "Cross Rhodes", "recap": "Family reunions bring together past and present as characters confront their histories. Old wounds are reopened while new healing begins."},
    (5, 17): {"season": 5, "episode": 17, "title": "The Princess Dowry", "recap": "Money and marriage intersect as financial considerations influence romantic decisions. The episode explores how wealth affects relationships and love."},
    (5, 18): {"season": 5, "episode": 18, "title": "Con-Heir", "recap": "Inheritance and legacy become central themes as characters deal with family wealth and responsibility. The episode examines the burden of privilege."},
    (5, 19): {"season": 5, "episode": 19, "title": "It Girl, Interrupted", "recap": "Mental health and treatment become important topics as characters seek professional help. The episode reduces stigma around therapy and medication."},
    (5, 20): {"season": 5, "episode": 20, "title": "Salon of the Dead", "recap": "Death and mourning affect the community as characters deal with loss. Grief brings people together while also revealing hidden tensions."},
    (5, 21): {"season": 5, "episode": 21, "title": "Despicable B", "recap": "Moral ambiguity reaches new heights as characters make questionable choices. The episode explores how good people can do bad things under pressure."},
    (5, 22): {"season": 5, "episode": 22, "title": "Raiders of the Lost Art", "recap": "Art and culture become battlegrounds for personal and professional rivalry. The episode examines how creativity can be both inspiring and destructive."},
    (5, 23): {"season": 5, "episode": 23, "title": "The Fugitives", "recap": "Characters go into hiding as consequences catch up with them. The episode explores themes of accountability and the impossibility of escaping the past."},
    (5, 24): {"season": 5, "episode": 24, "title": "The Return of the Ring", "recap": "Season finale brings engagement and commitment issues to the forefront. Characters must decide if they're ready for the next stage of their relationships."},

    # Season 6 (10 episodes) - Final Season
    (6, 1): {"season": 6, "episode": 1, "title": "Gone Maybe Gone", "recap": "The final season begins with major changes as characters have moved on with their lives. Five years later, everyone has evolved and new dynamics have emerged."},
    (6, 2): {"season": 6, "episode": 2, "title": "High Infidelity", "recap": "Marital problems and infidelity threaten established relationships. The episode explores how people change over time and whether love can survive growth and evolution."},
    (6, 3): {"season": 6, "episode": 3, "title": "Dirty Rotten Scandals", "recap": "Political scandals and public exposure affect personal relationships. The episode examines how private lives become public spectacle in the digital age."},
    (6, 4): {"season": 6, "episode": 4, "title": "Portrait of a Lady Alexander", "recap": "Art and artistic expression become ways to process emotion and experience. The episode explores how creativity helps people understand themselves and their relationships."},
    (6, 5): {"season": 6, "episode": 5, "title": "Monstrous Ball", "recap": "A costume ball brings out hidden sides of characters' personalities. Masks and disguises provide freedom to express suppressed desires and feelings."},
    (6, 6): {"season": 6, "episode": 6, "title": "Where the Vile Things Are", "recap": "Dark secrets from the past surface, threatening current relationships. The episode explores how past mistakes continue to influence present happiness."},
    (6, 7): {"season": 6, "episode": 7, "title": "Save the Last Chance", "recap": "Second chances and redemption become possible as characters confront their histories. The episode examines whether people can truly change and grow."},
    (6, 8): {"season": 6, "episode": 8, "title": "It's Really Complicated", "recap": "Relationship complications reach their peak as characters struggle with commitment and compatibility. The episode explores the difference between love and being in love."},
    (6, 9): {"season": 6, "episode": 9, "title": "The Revengers", "recap": "Revenge plots come to fruition as characters face the consequences of their actions. The episode examines whether revenge brings satisfaction or just perpetuates cycles of hurt."},
    (6, 10): {"season": 6, "episode": 10, "title": "New York, I Love You XOXO", "recap": "Series finale provides resolution for all major characters and relationships. Gossip Girl's true identity is finally revealed, bringing the story full circle as everyone gets their happy ending."}
}

@app.route('/recaps/season/<int:season>/episode/<int:episode>', methods=['GET'])
def get_episode_recap(season, episode):
    """
    Get episode recap for a specific season and episode
    
    Args:
        season (int): Season number
        episode (int): Episode number
        
    Returns:
        JSON response with episode data or error message
    """
    try:
        # Look up episode using tuple key
        episode_key = (season, episode)
        
        if episode_key in episode_recaps:
            episode_data = episode_recaps[episode_key]
            app.logger.info(f"Successfully retrieved recap for Season {season}, Episode {episode}")
            return jsonify(episode_data)
        else:
            app.logger.warning(f"Recap not found for Season {season}, Episode {episode}")
            return jsonify({"error": "Recap not found"}), 404
            
    except Exception as e:
        app.logger.error(f"Error retrieving recap: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint with API information
    """
    return jsonify({
        "message": "Gossip Girl Episode Recaps API",
        "usage": "GET /recaps/season/<season>/episode/<episode>",
        "example": "/recaps/season/1/episode/1",
        "available_episodes": len(episode_recaps),
        "seasons": list(set(key[0] for key in episode_recaps.keys()))
    })

@app.route('/recaps', methods=['GET'])
def list_all_recaps():
    """
    List all available episode recaps
    """
    episodes_list = []
    for (season, episode), data in episode_recaps.items():
        episodes_list.append({
            "season": season,
            "episode": episode,
            "title": data["title"],
            "endpoint": f"/recaps/season/{season}/episode/{episode}"
        })
    
    # Sort by season and episode
    episodes_list.sort(key=lambda x: (x["season"], x["episode"]))
    
    return jsonify({
        "total_episodes": len(episodes_list),
        "episodes": episodes_list
    })

@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.logger.info("Starting Gossip Girl Episode Recaps API")
    app.logger.info(f"Available episodes: {len(episode_recaps)}")
    app.run(host='0.0.0.0', port=5000, debug=True)
