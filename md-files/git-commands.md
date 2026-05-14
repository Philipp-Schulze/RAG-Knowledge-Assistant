# cheatsheet git

Category                        Action                          Command                                             Use Case

Setup                           Connect Original                git remote add upstream <original_url>              Do this once to link to the source repo.
Setup                           Check Remotes                   git remote -v                                       Verify both origin and upstream exist.

Update                          Fetch Changes                   git fetch upstream                                  Pull the latest data from the original repo.
Update                          Sync Main                       git checkout main && git merge upstream/main        Update your local code with original changes.

Work                            New Branch                      git checkout -b <branch_name>                       "Always work in a branch, never in main."

Submit                          Save Work                       git add . && git commit -m ""description""          Save your changes locally.
Submit                          Push to Fork                    git push origin <branch_name>                       Upload changes to your GitHub profile.

Clean                           Delete Branch                   git branch -d <branch_name>                         Remove local branch after PR is merged.