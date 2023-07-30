# 0x09. Web infrastructure design

## Concepts
For this project, we expect you to look at these concepts:

- DNS: 
  - Basics [Learn everything about DNS cartoon](https://howdns.works/)
  - Be sure to know the main DNS record types
	- [A](https://support.dnsimple.com/articles/a-record/)
	- [CNAME](https://en.wikipedia.org/wiki/CNAME_record)
	- [MX](https://en.wikipedia.org/wiki/MX_record)
	- [TXT](https://en.wikipedia.org/wiki/TXT_record)
  - Advanced
	- [Use DNS to scale with round-robin DNS](https://www.dnsknowledge.com/whatis/round-robin-dns/)
	- [What’s an NS Record?](https://support.dnsimple.com/articles/ns-record/)
	- [What’s an SOA Record?](https://support.dnsimple.com/articles/soa-record/)
- [Monitoring](https://intranet.alxswe.com/concepts/13)
- Web Server: [Wikipedia about web server](https://en.wikipedia.org/wiki/Web_server), [Web Server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server), [Waht is a web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)
- Network basics: [Protocol](https://www.techtarget.com/searchnetworking/definition/protocol), [Ip Addreaa](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm), [TCP/IP](https://www.avast.com/c-what-is-tcp-ip#), [IP Port](https://www.lifewire.com/port-numbers-on-computer-networks-817939)
- Load balancer: [Read 1](https://www.thegeekstuff.com/2016/01/load-balancer-intro/) and [Read 2](https://community.f5.com/t5/technical-articles/intro-to-load-balancing-for-developers-the-algorithms/ta-p/273759)
- Server: [Read](https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement), [watch video 1](https://www.youtube.com/watch?v=B1ANfsDyjeA) and [video 2](https://www.youtube.com/watch?t=33&v=iuqXFC_qIvA)

# Resources
### Read or watch:

- **Network basics** *concept page*
- **Server** *concept page*
- **Web server** *concept page*
- **DNS** *concept page*
- **Load balancer** *concept page*
- **Monitoring** *concept page*
- [What is a database](https://www.oracle.com/ke/database/what-is-database/)
- [What’s the difference between a web server and an app server?](https://www.infoworld.com/article/2077354/app-server-web-server-what-s-the-difference.html)
- [DNS record types](https://www.site24x7.com/learn/dns-record-types.html)
- [Single point of failure](https://avinetworks.com/glossary/single-point-of-failure/)
- [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
- [What is HTTPS](https://www.instantssl.com/http-vs-https)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
- You must be able to explain what each component is doing
- You must be able to explain system redundancy
- Know all the mentioned acronyms: LAMP, SPOF, QPS

### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.


# Requirements
### General
- A README.md file, at the root of the folder of the project, is mandatory
- For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
- This project will be manually reviewed:
- As each task is completed, the name of that task will turn green
- Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use imgur but feel free to use anything you want).
- For the following tasks, insert the link from of your screenshot into the answer file
- After pushing your answer file to GitHub, insert the GitHub file link into the URL box
- You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
- Focus on what you are being asked:
- Cover what the requirements mention, we will explore details in a later project
- Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
- Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
- In this project, again, avoid going in details if not asked
