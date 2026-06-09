# cloud-project
During the Spring '26 semester, I took an EEP wherein I worked on one major project, and two sub-projects. This is the main project that I worked on.
This will serve as the writeup for the project, as well as the long version of what my site contains.<br>
this formatting is subject to change, i'm just trying to get a general idea down for now

---

## Project Goals
The goals that I had are two-fold:
1. Learn and apply server access and networking fundamentals
2. Study the speeds of cloud reading and writing across Wi-Fi protocols

---

## Methodology
Use fio (hyperlink), wrote and read from cloud

---

## Challenges faced
### Accessing the Server
This was the largest issue that I've had during the project itself. During the beginning of the project, my core objection was to leave port 22 alone such that the server would be privately accessible through a VPN, and only accessible through a VPN.<br>
The first attempt was to use Tailscale (use hyperlink), an extremely easy to use VPN service where you can access another machine on the same tailnet.<br>
The second attempt was to use cloudflared (use hyperlink)
The last attempt, and ultimately the solution, was to just open port 22.

