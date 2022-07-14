# PasswordCracker
DSP (Digital Systems Project): Password Cracking Tool

## Abstract 

Ethical hackers have a variety of tools and programs that they use to perform penetration tests, most of which come in the form of a CLI (Command Line Interface). With so many programs that are written in a CLI there many different commands they have to remember. One common tool amongst these are Password Crackers which, as the name implies, will crack a hashed password which would be stored on a database. We will be developing a GUI version of a password cracker to try lift the load off ethical hacker so that they do not have to remember so many commands and can just focus on being fast and efficient. 

## Introduction
Passwords are widely used for user authentication and will likely remain in use in the foreseeable future, despite several weaknesses. One important weakness is that human generated passwords are far from being random, which makes them susceptible to guessing attacks (Dürmuth, 2015). These attacks can range from brute forcing, Dictionary attacks and Markov chains which have different uses and effectiveness. For example, the Markov modelling technique from natural language processing is used to dramatically reduce the size of the password space to be searched (Narayanan, Shmatikov, 2005). White-hat hackers use tools like Hashcat and John the Ripper to test password security when staging a Penetration test. Penetration testing is the act of testing a system or systems for vulnerabilities due to improper system or hardware configuration and software faults that should be mitigated against. (Hussain, 2017). These tools are used on a frequent basis to perform offline password cracking. Having a fast and efficient tool while still providing the user will a clean GUI design can be achieved over a CLI design with large amount of documentation and hard to read commands. Offline password cracking tools can also be used for system administration work to try and crack employee passwords to find insecure passwords. The goal for the project is to design and develop an offline password cracking GUI that is easy to use while still providing fully password cracking functionalities. 


# Description
This is a Password Cracking Tool that is being developed for my final year project in University.

# Features
-----------------------
## Attack Algorithms 
-----------------------
- Brute Force
- Dictionary Attack
- Hybrid Dictionary Attack
- Rule-Based Attack
- RainbowTable Attack
- Markov Chain Attack

-----------------------
## Others
- Auto Detect Hash value
- Save and Load an attack
- Load a single or multiple hash values to crack at once

