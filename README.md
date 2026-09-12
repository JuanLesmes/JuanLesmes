<!--
  ╭────────────────────────────────────────────────────────────────────╮
  │  README de perfil · repositorio JuanLesmes/JuanLesmes               │
  │                                                                     │
  │  Reemplazar antes de publicar:                                      │
  │    TU-LINKEDIN · TU-CORREO · URL-PSYCONOVA · URL-IMPERIO-REAL       │
  │                                                                     │
  │  La serpiente 🐍 (sección "Contribuciones") necesita el workflow    │
  │  .github/workflows/snake.yml (archivo aparte).                      │
  ╰────────────────────────────────────────────────────────────────────╯
-->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff7a18,40:ffb347,75:ff3d77,100:7b2ff7&height=240&section=header&text=Juan%20Fernando%20Lesmes&fontSize=48&fontColor=ffffff&fontAlignY=35&desc=Systems%20Engineer%20%C2%B7%20Ingeniero%20de%20Sistemas%20%C2%B7%20Bogot%C3%A1%2C%20Colombia&descAlignY=57&descSize=18&animation=fadeIn" width="100%" alt="Juan Fernando Lesmes — Systems Engineer"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=FF7A18&center=true&vCenter=true&width=760&height=48&lines=Construyo+software+que+simplifica+negocios;I+build+software+that+simplifies+businesses;ERP+%C2%B7+POS+%C2%B7+Inventarios+%C2%B7+Web+apps;Python+%C2%B7+FastAPI+%C2%B7+TypeScript+%C2%B7+Angular+%C2%B7+Next.js;Freelance+desde+2025+%C2%B7+Bogot%C3%A1%2C+Colombia" alt="Construyo software que simplifica negocios"/>

<br/>

<a href="https://www.linkedin.com/in/TU-LINKEDIN"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
&nbsp;
<a href="mailto:TU-CORREO"><img src="https://img.shields.io/badge/Email-FF7A18?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
&nbsp;
<a href="https://github.com/JuanLesmes?tab=repositories"><img src="https://img.shields.io/badge/Repos-FF3D77?style=for-the-badge&logo=github&logoColor=white" alt="Repositorios"/></a>
&nbsp;
<img src="https://komarev.com/ghpvc/?username=JuanLesmes&style=for-the-badge&color=ffb347&label=VISITAS" alt="Visitas al perfil"/>

<br/><br/>

<sub>🇪🇸 Español &nbsp;|&nbsp; 🇬🇧 <i>English in italics</i></sub>

</div>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff7a18,50:ff3d77,100:7b2ff7&height=3" width="100%" alt=""/>

## 🧭 Sobre mí · About me

```bash
$ curl -s https://github.com/JuanLesmes/api/about | jq
```

```json
{
  "status": 200,
  "name": "Juan Fernando Lesmes Castañeda",
  "role": ["Systems Engineer", "Software Developer"],
  "education": "Ingeniería de Sistemas · Pontificia Universidad Javeriana · 2025",
  "based_in": "Bogotá, Colombia 🇨🇴",
  "building": ["ERP", "POS", "inventory systems", "web apps", "internal tools"],
  "previously": "IT lead en una firma de abogados (2022–2024)",
  "likes": ["software que resuelve problemas reales", "APIs limpias", "despliegues reproducibles"],
  "open_to": ["backend / full-stack roles", "freelance projects", "AI engineering"]
}
```

Ingeniero de Sistemas de la Javeriana. Desde 2025 trabajo freelance construyendo sistemas de inventario, POS y ERP para pequeñas y medianas empresas, además de sitios web y herramientas internas para firmas de abogados. Me gusta el software que resuelve problemas reales: rápido de usar, fácil de mantener y que sigue funcionando aunque se caiga el internet.

*Systems Engineer (Javeriana). Since 2025 I've worked freelance building inventory, POS and ERP systems for small and medium businesses, plus websites and internal tools for law firms. I like software that solves real problems: fast to use, easy to maintain, and still working when the internet goes down.*

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff7a18,50:ff3d77,100:7b2ff7&height=3" width="100%" alt=""/>

## 🧰 Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,fastapi,ts,js,nodejs,angular,react,nextjs,cs,dotnet,postgres,sqlite,docker,aws,azure,cloudflare,linux,git,powershell,vscode&perline=10" alt="Tech stack"/>

</div>

| &nbsp; | Herramientas · Tools |
|:--|:--|
| ⚙️ **Backend** | Python 3.12 · FastAPI · Pydantic v2 · TypeScript · Node.js · pytest |
| 🖥️ **Frontend** | Angular · Next.js (App Router, RSC) · React · SCSS · RxJS · PWA / service workers |
| 🗄️ **Datos · Data** | PostgreSQL · SQLite (modo WAL) · diseño de esquemas · *schema design* |
| 🚀 **Infra & DevOps** | Docker Compose · Caddy + Let's Encrypt · Cloudflare DNS · VPS Ubuntu · Backblaze B2 · PowerShell |
| ☁️ **Cloud** | AWS · Azure |
| 🤖 **AI-assisted dev** | Claude Code y LLMs para acelerar el desarrollo · *to speed up development* |

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff7a18,50:ff3d77,100:7b2ff7&height=3" width="100%" alt=""/>

## 🚀 Proyectos destacados · Featured work

<table>
<tr>
<td width="50%" valign="top">

### ⚖️ Gestor de procesos judiciales
<sub>🔒 Proyecto privado para una firma de abogados · <i>Private client project</i></sub>

Usuarios y roles, filtros y consulta automática de procesos en la **Rama Judicial** (API CPNU): búsqueda por radicado, actuaciones paginadas, deduplicación y caché. 116 pruebas con pytest, despliegue con Docker Compose + Caddy (HTTPS automático) en un VPS, DNS en Cloudflare y backups en Backblaze B2.

*Users & roles, filters and automatic case lookup on Colombia's judicial-branch API: search by case number, paginated proceedings, de-duplication and caching. 116 pytest tests, deployed with Docker Compose + Caddy (auto HTTPS) on a VPS, Cloudflare DNS and Backblaze B2 backups.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat-square&logo=cloudflare&logoColor=white)

</td>
<td width="50%" valign="top">

### 🧾 ERP + POS para MIPYMEs
<sub>🔒 Producto comercial · <i>Commercial product</i></sub>

Inventario, ventas, control de caja y punto de venta para pequeñas y medianas empresas. Multi-tenant desde el día uno, operaciones idempotentes y modo offline (PWA) para que la venta no se detenga sin internet.

*Inventory, sales, cash control and point-of-sale for SMEs. Multi-tenant from day one, idempotent operations and an offline mode (PWA) so sales never stop when the connection drops.*

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![PWA](https://img.shields.io/badge/PWA-5A0FC8?style=flat-square&logo=pwa&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🥗 RecetarioVEG
<sub>📂 <a href="https://github.com/JuanLesmes/RecetarioVEG">Ver repositorio · View repo</a></sub>

121 recetas veganas y vegetarianas pensadas para Colombia: ingredientes como se piden en la plaza, buscador por lo que tienes en la nevera, lista de mercado y planificador semanal.

*121 vegan and vegetarian recipes made for Colombia: ingredients as you'd ask for them at the market, search by what's in your fridge, shopping list and weekly planner.*

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)

</td>
<td width="50%" valign="top">

### 📦 Sistemas de inventario · Inventory systems
<sub>📂 <a href="https://github.com/JuanLesmes/GestionInventario">GestionInventario</a> · <a href="https://github.com/JuanLesmes/InventarioApp">InventarioApp</a></sub>

Dos apps de escritorio para gestionar inventarios: una en Python (patrón MVC, interfaz gráfica y SQLite embebida) y otra en C#.

*Two desktop inventory apps: one in Python (MVC pattern, GUI and embedded SQLite) and one in C#.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 🌐 Sitios web · Websites

**[Psyconova](URL-PSYCONOVA)** — Angular 21 · TypeScript · SCSS · RxJS &nbsp;&nbsp;|&nbsp;&nbsp; **[Imperio Real Abogados](URL-IMPERIO-REAL)** — Next.js 14 (App Router, RSC) · React 18 · TypeScript

</td>
</tr>
</table>

> 🥗 **Dato curioso · Fun fact:** el mismo cerebro que diseña inventarios para negocios también hizo un buscador de recetas por lo que hay en la nevera. Al final, todo es gestión de inventario.
> *The same brain that designs inventory systems for businesses also built a recipe search by what's in your fridge. In the end, everything is inventory management.*

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff7a18,50:ff3d77,100:7b2ff7&height=3" width="100%" alt=""/>

## 🧱 Cómo construyo · How I build

- **Monolito modular antes que microservicios.** · *Modular monolith before microservices.*
- **Idempotencia en toda operación que cambia estado.** · *Idempotency keys on every state-changing operation.*
- **`numeric`, nunca `float`, para dinero y cantidades.** · *`numeric`, never `float`, for money and quantities.*
- **Offline-first cuando el negocio lo necesita:** PWA, service workers y sincronización idempotente. · *Offline-first when the business needs it.*
- **Seguro por defecto:** sesiones, CSP, HSTS y contraseñas con scrypt. · *Secure by default.*
- **Pruebas y despliegues reproducibles:** pytest, Docker Compose y backups automáticos. · *Tests and reproducible deploys.*

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff7a18,50:ff3d77,100:7b2ff7&height=3" width="100%" alt=""/>

## 📍 Ahora · Now

- 💼 Freelance: sistemas de inventario, POS y ERP para pymes, más webs y herramientas internas · *Freelance: inventory, POS & ERP systems for SMEs, plus websites and internal tools*
- 📚 Aprendiendo: agentes de IA con LangGraph y Amazon Bedrock · *Learning: AI agents with LangGraph and Amazon Bedrock*
- 🤝 Abierto a roles backend / full-stack y proyectos freelance · *Open to backend / full-stack roles and freelance projects*
- 📬 Escríbeme · *Reach out:* [TU-CORREO](mailto:TU-CORREO)

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff7a18,50:ff3d77,100:7b2ff7&height=3" width="100%" alt=""/>

## 📊 GitHub

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=JuanLesmes&show_icons=true&include_all_commits=true&hide_border=true&bg_color=0d1117&title_color=ffb347&icon_color=ff7a18&text_color=c9d1d9&rank_icon=github">
  <img height="165" alt="GitHub stats" src="https://github-readme-stats.vercel.app/api?username=JuanLesmes&show_icons=true&include_all_commits=true&hide_border=true&bg_color=ffffff&title_color=ff7a18&icon_color=ff3d77&text_color=24292f&rank_icon=github">
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=JuanLesmes&layout=compact&hide=tex&langs_count=8&hide_border=true&bg_color=0d1117&title_color=ffb347&text_color=c9d1d9">
  <img height="165" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=JuanLesmes&layout=compact&hide=tex&langs_count=8&hide_border=true&bg_color=ffffff&title_color=ff7a18&text_color=24292f">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=JuanLesmes&hide_border=true&background=0d1117&ring=ff7a18&fire=ff3d77&currStreakLabel=ffb347&currStreakNum=ffffff&sideLabels=ffb347&sideNums=ffffff&dates=8b949e">
  <img alt="GitHub streak" src="https://streak-stats.demolab.com?user=JuanLesmes&hide_border=true&background=ffffff&ring=ff7a18&fire=ff3d77&currStreakLabel=ff7a18&currStreakNum=24292f&sideLabels=ff7a18&sideNums=24292f&dates=57606a">
</picture>

### 🐍 Contribuciones · Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JuanLesmes/JuanLesmes/output/snake-dark.svg">
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/JuanLesmes/JuanLesmes/output/snake.svg">
</picture>

</div>

<br/>

<div align="center">

<sub>Hecho con ☕ en Bogotá · <i>Made with ☕ in Bogotá</i></sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7b2ff7,25:ff3d77,60:ffb347,100:ff7a18&height=120&section=footer&animation=twinkling" width="100%" alt=""/>

</div>
