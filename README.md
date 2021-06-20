Here we store all that is needed (and not stored in the GiRaFFE Bitbucket repo) for reproducing simulations of BBH mergers in the context of force-free magnetic field topologies, and analyzing resulting data, including:

* Data analysis scripts
* Visit visualization scripts,
* Einstein Toolkit parameter files, 
* etc.

**Starting out for the first time:**

Log in to Bitbucket, then click on the repository named
"black_hole_binaries_in_magnetized_plasmas", then click on the "..." icon in
the upper-left corner, then click the "Clone" button. 

The command for cloning is right there. Paste it into your Linux terminal.

===============================

Pulling the latest revision:

Go to the directory you created for the git clone originally then type

git pull 


===============================

Pushing your latest changes:

Specify the filename you'd like to commit.
git add [filename]

Then to push your latest changes, first write a commit message.
For example:

git commit -m "Add the LaTeX paper, which includes a draft of the Intro, Basic Equations, and Computational Techniques sections. Also the Results section is started."

Finally push the changes :

git push -u origin master