# cheatsheet docker

Category            Action                  Command                                                 Use Case

Global              Start Stack             docker compose up -d                                    Launch everything in the background.
Global              Rebuild & Start         docker compose up -d --build                            Apply code changes to all containers.
Global              Stop Stack              docker compose stop                                     Pause services (saves state/data).
Global              Tear Down               docker compose down                                     Stop and remove containers/networks.
Global              Nuke Everything         docker compose down -v --rmi local                      "Wipe containers, volumes, and local images."

Service             Start Service           docker compose up -d <name>                             "Start just one (e.g., rag_retrieval)."
Service             Stop Service            docker compose stop <name>                              Stop just one without affecting others.
Service             Restart Service         docker compose restart <name>                           Quick reboot of a specific container.
Service             Rebuild Service         docker compose up -d --build <name>                     Update only one service after code changes.

Logs                All Logs                docker compose logs -f                                  Stream live output from the whole stack.
Logs                Service Logs            docker compose logs -f <name>                           "Debug a specific service (e.g., rag_gen)."

Inspect             List Status             docker compose ps                                       Check which containers are Up or Exited.
Inspect             Resource Usage          docker stats                                            Monitor RAM/CPU usage (crucial for LLMs).
Inspect             Shell Access            docker compose exec -it <name> /bin/bash                Open a terminal inside a container.

Ollama              List Models             docker compose exec -it rag_ollama ollama list          "Verify downloaded weights (e.g., Qwen)."
Ollama              Pull Model              docker compose exec -it rag_ollama ollama pull <m>      Manually download a new model.