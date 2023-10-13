12-10-2023

1. Overview
Kryxa is an application to manage an internet cafe. With inspiration from SENET, LAN center software for managing PCs and consoles. Vietnam have a big number of cybercafe, according to gamek.vn 23/10/2018 10:30 PM, there is around 45.000 cybercafe in Vietnam. Therefore, the need for a software service to manage cybercafe is essential.
Our app will be a locally hosted server with web frontend with 2 main actors:
- Admin: Staffs, IT admin.
- User: players, esport organization.
Target environment is Windows. 
2. Key features:
- Admin:
	- Assign PCs for users:
		- Create/remove PCs.
		- Admin choose a PCs from GUI to open a session for user.
		- Sessions have time limit and can be extended or terminated.
	- Manage sales, items, billing for customers
		- When a session is over or terminated, generate a bill for customer.
		- Add/remove items on sale.
	- View sales, history, statistics:
		- View sales for each item
		- Time usage per PCs
		- Graphs, visualization (potential)
	- Report issues, bugs:
		- Create bug report
	- Create tournament (potential)
- User:
	- Buy items:
		- Can buy food, drinks, etc.
		- Extend session
	- View timer for session
	- View bill
	- Report issues
		- Technical issues
		- Service issues
3. Tech stack:
- Frontend: (Lead: An (layout), Khiem (logic))
	- HTML/CSS: use TailwindCSS for CSS framework
	- Svelte: front-end framework
- Backend: (Lead: Triet)
	- Python / FastApi
	- SQLite
	- Swagger docs (for api documentation)
- UI/UX design: (Lead: Bao)
	- Figma
- Test: (Lead: Minh)
	- API test: Postman, curl
	- Frontend: rice based system
4. Planning:
- 13/10/2023 - 20/10/2023:
	- Complete PA0
	- Setup tools
- 13/10/2023 - 27/10/2023:
	- Design data schema
	- General interaction with data
	- Self training
	- Seminar for code training:
		- 17/10/2023: Backend intro (Python, FastAPI, HTTP requests)
		- 20/10/2023: Frontend intro (HTML, CSS, JS, Svelte, Tailwind)