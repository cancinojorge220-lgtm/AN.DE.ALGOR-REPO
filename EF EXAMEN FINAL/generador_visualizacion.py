import json
import os
import webbrowser

def generar_html_interactivo(historial_pasos, almacenes_coordenadas, conexiones_red, vias_bloqueadas):
    pasos_json = json.dumps(historial_pasos, ensure_ascii=False)
    coordenadas_json = json.dumps(almacenes_coordenadas, ensure_ascii=False)
    conexiones_json = json.dumps(conexiones_red, ensure_ascii=False)
    bloqueos_lista = [[u, v] for u, v in vias_bloqueadas]
    bloqueos_json = json.dumps(bloqueos_lista, ensure_ascii=False)
    
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulador de Backtracking - Logística Andina</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0f172a;
            --panel-bg: #1e293b;
            --accent-green: #10b981;
            --accent-red: #ef4444;
            --accent-blue: #3b82f6;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #334155;
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Outfit', sans-serif;
        }}
        
        body {{
            background-color: var(--bg-color);
            color: var(--text-main);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}
        
        header {{
            background-color: var(--panel-bg);
            padding: 15px 30px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        header h1 {{
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(to right, #60a5fa, #34d399);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        header p {{
            font-size: 0.875rem;
            color: var(--text-muted);
        }}
        
        .container {{
            flex: 1;
            display: flex;
            height: calc(100vh - 70px);
        }}
        
        .sidebar {{
            width: 420px;
            background-color: var(--panel-bg);
            border-right: 1px solid var(--border-color);
            padding: 25px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            overflow-y: auto;
        }}
        
        .map-area {{
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #0b0f19;
            position: relative;
            padding: 20px;
        }}
        
        .control-panel {{
            background: #151f32;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        
        .controls {{
            display: flex;
            gap: 10px;
            justify-content: center;
        }}
        
        button {{
            background-color: #334155;
            color: var(--text-main);
            border: none;
            padding: 10px 18px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        button:hover {{
            background-color: #475569;
        }}
        
        button.primary {{
            background-color: var(--accent-blue);
        }}
        
        button.primary:hover {{
            background-color: #2563eb;
        }}
        
        button.success {{
            background-color: var(--accent-green);
        }}
        
        button.success:hover {{
            background-color: #059669;
        }}
        
        .progress-bar-container {{
            width: 100%;
            background-color: #334155;
            height: 6px;
            border-radius: 3px;
            overflow: hidden;
            margin-top: 5px;
        }}
        
        .progress-bar {{
            height: 100%;
            background-color: var(--accent-blue);
            width: 0%;
            transition: width 0.1s ease;
        }}
        
        .status-box {{
            flex: 1;
            background: #0f172a;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 15px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 10px;
            font-size: 0.9rem;
        }}
        
        .status-header {{
            font-weight: bold;
            color: var(--accent-blue);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 5px;
            font-size: 0.95rem;
            display: flex;
            justify-content: space-between;
        }}
        
        .log-entry {{
            padding: 8px 12px;
            border-radius: 6px;
            border-left: 4px solid var(--border-color);
            background-color: #1e293b;
            line-height: 1.4;
            animation: fadeIn 0.3s ease;
        }}
        
        .log-entry.evaluar {{
            border-left-color: #f59e0b;
        }}
        
        .log-entry.avanzar {{
            border-left-color: var(--accent-green);
            background-color: #064e3b;
        }}
        
        .log-entry.backtrack {{
            border-left-color: #a855f7;
            background-color: #3b0764;
        }}
        
        .log-entry.rechazado {{
            border-left-color: var(--accent-red);
            opacity: 0.7;
        }}
        
        .log-entry.exito {{
            border-left-color: var(--accent-blue);
            background-color: #1e3a8a;
            font-weight: bold;
        }}
        
        #map-svg {{
            width: 100%;
            height: 100%;
            max-width: 650px;
            max-height: 650px;
        }}
        
        .node {{
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        
        .node circle {{
            fill: #1e293b;
            stroke: #475569;
            stroke-width: 3px;
            transition: all 0.3s ease;
        }}
        
        .node text {{
            fill: var(--text-main);
            font-size: 13px;
            font-weight: bold;
            text-anchor: middle;
            pointer-events: none;
            text-shadow: 0 2px 4px rgba(0,0,0,0.8);
        }}
        
        /* Modos dinámicos de nodos */
        .node.target circle {{
            stroke: #94a3b8;
            stroke-dasharray: 4;
        }}
        
        .node.active circle {{
            fill: #3b82f6;
            stroke: #60a5fa;
            filter: drop-shadow(0 0 8px #3b82f6);
            stroke-width: 4px;
        }}
        
        .node.visited circle {{
            fill: var(--accent-green);
            stroke: #34d399;
            filter: drop-shadow(0 0 6px rgba(16, 185, 129, 0.4));
        }}
        
        .node.backtracked circle {{
            fill: #a855f7;
            stroke: #c084fc;
        }}
        
        .link {{
            stroke: #334155;
            stroke-width: 3px;
            stroke-linecap: round;
            transition: all 0.3s ease;
        }}
        
        .link.active {{
            stroke: var(--accent-green);
            stroke-width: 5px;
            filter: drop-shadow(0 0 4px var(--accent-green));
        }}
        
        .link.evaluating {{
            stroke: #f59e0b;
            stroke-width: 5px;
            stroke-dasharray: 8 4;
            animation: dash 1s linear infinite;
        }}
        
        .link.blocked {{
            stroke: var(--accent-red);
            stroke-width: 2px;
            stroke-dasharray: 4 4;
            opacity: 0.6;
        }}
        
        .link.backtrack-link {{
            stroke: #a855f7;
            stroke-width: 4px;
        }}
        
        @keyframes dash {{
            to {{
                stroke-dashoffset: -20;
            }}
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(5px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .legend-box {{
            background: #151f32;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 12px;
            font-size: 0.8rem;
            display: flex;
            flex-wrap: wrap;
            gap: 10px 15px;
        }}
        
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        
        .legend-color {{
            width: 14px;
            height: 14px;
            border-radius: 50%;
            display: inline-block;
        }}
        
        .legend-line {{
            width: 20px;
            height: 4px;
            border-radius: 2px;
            display: inline-block;
        }}
    </style>
</head>
<body>
    <header>
        <div>
            <h1>Simulador Interactivo de Backtracking</h1>
            <p>Logística Andina S.A.C. - Distribución Escolar de Equipos</p>
        </div>
        <div>
            <span style="font-weight: 600; color: var(--accent-green);">Camino Hamiltoniano</span>
        </div>
    </header>
    
    <div class="container">
        <div class="sidebar">
            <div class="control-panel">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-weight: 600; font-size: 0.95rem;">Controles de Simulación</span>
                    <span id="step-counter" style="font-size: 0.85rem; color: var(--text-muted);">Paso 0 / 0</span>
                </div>
                
                <div class="progress-bar-container">
                    <div id="progress" class="progress-bar"></div>
                </div>
                
                <div class="controls">
                    <button id="btn-prev" title="Paso Anterior">◀</button>
                    <button id="btn-play" class="primary" title="Reproducir/Pausar">Reproducir ▶</button>
                    <button id="btn-next" title="Siguiente Paso">▶</button>
                    <button id="btn-reset" class="success" title="Reiniciar">Reiniciar ⟲</button>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem;">
                    <span>Velocidad:</span>
                    <select id="select-speed" style="background:#334155; color:white; border:none; padding:4px; border-radius:4px; cursor:pointer;">
                        <option value="1200">Lento (1.2s)</option>
                        <option value="700">Medio (0.7s)</option>
                        <option value="350" selected>Rápido (0.35s)</option>
                        <option value="120">Veloz (0.12s)</option>
                        <option value="50">Turbo (0.05s)</option>
                    </select>
                </div>
                
                <div style="display: flex; align-items: center; gap: 8px; font-size: 0.8rem; margin-top: 5px; border-top: 1px solid var(--border-color); padding-top: 10px;">
                    <input type="checkbox" id="chk-solo-clave" checked style="cursor:pointer; width:15px; height:15px;">
                    <label for="chk-solo-clave" style="cursor:pointer; font-weight:600; color:var(--accent-green);">Modo Exposición (Solo pasos clave)</label>
                </div>
            </div>
            
            <div class="status-box">
                <div class="status-header">
                    <span>Bitácora de Logística</span>
                    <span id="operation-type" style="text-transform: uppercase; font-size: 0.75rem; letter-spacing: 1px;">-</span>
                </div>
                <div id="log-content" style="display:flex; flex-direction:column; gap:10px;">
                    <!-- Los logs dinámicos se inyectan acá -->
                </div>
            </div>
            
            <div class="legend-box">
                <div class="legend-item">
                    <span class="legend-color" style="background: var(--accent-blue);"></span> Activo (Actual)
                </div>
                <div class="legend-item">
                    <span class="legend-color" style="background: var(--accent-green);"></span> Visitado
                </div>
                <div class="legend-item">
                    <span class="legend-color" style="background: #a855f7;"></span> Retroceso
                </div>
                <div class="legend-item">
                    <span class="legend-line" style="background: var(--accent-green);"></span> Vía Habilitada
                </div>
                <div class="legend-item">
                    <span class="legend-line" style="background: #f59e0b; border-top: 2px dashed #f59e0b;"></span> Evaluando Vía
                </div>
                <div class="legend-item">
                    <span class="legend-line" style="background: var(--accent-red); border-top: 2px dotted var(--accent-red);"></span> Vía Bloqueada
                </div>
            </div>
        </div>
        
        <div class="map-area">
            <svg id="map-svg" viewBox="0 0 600 650">
                <defs>
                    <marker id="arrow-green" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--accent-green)" />
                    </marker>
                    <marker id="arrow-orange" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b" />
                    </marker>
                    <marker id="arrow-purple" viewBox="0 0 10 10" refX="22" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#a855f7" />
                    </marker>
                </defs>
                <g id="links-group"></g>
                <g id="nodes-group"></g>
            </svg>
        </div>
    </div>
    
    <script>
        // Datos inyectados desde Python
        const pasosTodos = {pasos_json};
        const coordenadas = {coordenadas_json};
        const conexiones = {conexiones_json};
        const bloqueos = {bloqueos_json};
        
        let pasos = pasosTodos;
        let indexPasoActual = -1;
        let playingInterval = null;
        
        const chkSoloClave = document.getElementById("chk-solo-clave");
        
        function aplicarFiltro() {{
            if (chkSoloClave.checked) {{
                pasos = pasosTodos.filter(p => p.tipo === "avanzar" || p.tipo === "backtrack" || p.tipo === "exito");
            }} else {{
                pasos = pasosTodos;
            }}
            indexPasoActual = -1;
            actualizarVisualizacion();
        }}
        
        chkSoloClave.addEventListener("change", () => {{
            if (playingInterval) pausar();
            aplicarFiltro();
        }});
        
        // Elementos DOM
        const svg = document.getElementById("map-svg");
        const nodesGroup = document.getElementById("nodes-group");
        const linksGroup = document.getElementById("links-group");
        const logContent = document.getElementById("log-content");
        const stepCounter = document.getElementById("step-counter");
        const progress = document.getElementById("progress");
        const operationType = document.getElementById("operation-type");
        
        const btnPrev = document.getElementById("btn-prev");
        const btnPlay = document.getElementById("btn-play");
        const btnNext = document.getElementById("btn-next");
        const btnReset = document.getElementById("btn-reset");
        const selectSpeed = document.getElementById("select-speed");
        
        // Inicializar Grafo en SVG
        function inicializarGrafo() {{
            linksGroup.innerHTML = '';
            nodesGroup.innerHTML = '';
            
            const enlacesDibujados = new Set();
            
            Object.keys(conexiones).forEach(origen => {{
                conexiones[origen].forEach(destino => {{
                    const claveEnlace = [origen, destino].sort().join('-');
                    if (!enlacesDibujados.has(claveEnlace)) {{
                        enlacesDibujados.add(claveEnlace);
                        
                        const c1 = coordenadas[origen];
                        const c2 = coordenadas[destino];
                        
                        const esBloqueado = bloqueos.some(b => 
                            (b[0] === origen && b[1] === destino) || (b[0] === destino && b[1] === origen)
                        );
                        
                        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                        line.setAttribute("x1", c1.x);
                        line.setAttribute("y1", c1.y);
                        line.setAttribute("x2", c2.x);
                        line.setAttribute("y2", c2.y);
                        line.setAttribute("class", esBloqueado ? "link blocked" : "link");
                        line.setAttribute("id", `link-${{origen.replace('.', '')}}-${{destino.replace('.', '')}}`);
                        linksGroup.appendChild(line);
                    }}
                }});
            }});
            
            Object.keys(coordenadas).forEach(nombre => {{
                const coord = coordenadas[nombre];
                const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
                g.setAttribute("class", "node target");
                g.setAttribute("id", `node-${{nombre.replace('.', '')}}`);
                
                const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                circle.setAttribute("cx", coord.x);
                circle.setAttribute("cy", coord.y);
                circle.setAttribute("r", 20);
                
                const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
                text.setAttribute("x", coord.x);
                text.setAttribute("y", coord.y + 35);
                text.textContent = nombre;
                
                const label = document.createElementNS("http://www.w3.org/2000/svg", "text");
                label.setAttribute("x", coord.x);
                label.setAttribute("y", coord.y + 5);
                label.setAttribute("fill", "white");
                label.setAttribute("style", "font-size:10px;");
                label.textContent = nombre.replace("A.", "");
                
                g.appendChild(circle);
                g.appendChild(text);
                g.appendChild(label);
                nodesGroup.appendChild(g);
            }});
        }}
        
        function actualizarVisualizacion() {{
            document.querySelectorAll(".node").forEach(n => n.setAttribute("class", "node target"));
            document.querySelectorAll(".link").forEach(l => {{
                const claseOriginal = l.getAttribute("class");
                if (claseOriginal.includes("blocked")) {{
                    l.setAttribute("class", "link blocked");
                }} else {{
                    l.setAttribute("class", "link");
                }}
            }});
            
            if (indexPasoActual === -1) {{
                logContent.innerHTML = '<div class="log-entry">Haz click en "Siguiente" o "Reproducir" para iniciar la distribución.</div>';
                stepCounter.textContent = `Paso 0 / ${{pasos.length}}`;
                progress.style.width = "0%";
                operationType.textContent = "ESPERA";
                operationType.style.color = "var(--text-muted)";
                return;
            }}
            
            const paso = pasos[indexPasoActual];
            stepCounter.textContent = `Paso ${{indexPasoActual + 1}} / ${{pasos.length}}`;
            progress.style.width = `${{((indexPasoActual + 1) / pasos.length) * 100}}%`;
            operationType.textContent = paso.tipo;
            
            let colorTipo = "var(--text-muted)";
            if (paso.tipo === "evaluar") colorTipo = "#f59e0b";
            if (paso.tipo === "avanzar") colorTipo = "var(--accent-green)";
            if (paso.tipo === "backtrack") colorTipo = "#a855f7";
            if (paso.tipo === "rechazado") colorTipo = "var(--accent-red)";
            if (paso.tipo === "exito") colorTipo = "var(--accent-blue)";
            operationType.style.color = colorTipo;
            
            const logItem = document.createElement("div");
            logItem.className = `log-entry ${{paso.tipo}}`;
            logItem.innerHTML = `<strong>Paso ${{indexPasoActual + 1}}:</strong> ${{paso.mensaje}}`;
            logContent.innerHTML = '';
            logContent.appendChild(logItem);
            
            const ruta = paso.visitados;
            for (let i = 0; i < ruta.length; i++) {{
                const nodo = document.getElementById(`node-${{ruta[i].replace('.', '')}}`);
                if (nodo) {{
                    nodo.setAttribute("class", "node visited");
                }}
                
                if (i > 0) {{
                    const origen = ruta[i-1];
                    const destino = ruta[i];
                    const line1 = document.getElementById(`link-${{origen.replace('.', '')}}-${{destino.replace('.', '')}}`);
                    const line2 = document.getElementById(`link-${{destino.replace('.', '')}}-${{origen.replace('.', '')}}`);
                    if (line1) line1.setAttribute("class", "link active");
                    if (line2) line2.setAttribute("class", "link active");
                }}
            }}
            
            const nodoActivo = document.getElementById(`node-${{paso.origen.replace('.', '')}}`);
            if (nodoActivo) {{
                nodoActivo.setAttribute("class", "node active");
            }}
            
            if (paso.tipo === "evaluar" && paso.destino) {{
                const line1 = document.getElementById(`link-${{paso.origen.replace('.', '')}}-${{paso.destino.replace('.', '')}}`);
                const line2 = document.getElementById(`link-${{paso.destino.replace('.', '')}}-${{paso.origen.replace('.', '')}}`);
                if (line1) line1.setAttribute("class", "link evaluating");
                if (line2) line2.setAttribute("class", "link evaluating");
                
                const nodoEval = document.getElementById(`node-${{paso.destino.replace('.', '')}}`);
                if (nodoEval) nodoEval.setAttribute("class", "node target active-eval");
            }}
            
            if (paso.tipo === "backtrack" && paso.destino) {{
                const line1 = document.getElementById(`link-${{paso.origen.replace('.', '')}}-${{paso.destino.replace('.', '')}}`);
                const line2 = document.getElementById(`link-${{paso.destino.replace('.', '')}}-${{paso.origen.replace('.', '')}}`);
                if (line1) line1.setAttribute("class", "link backtrack-link");
                if (line2) line2.setAttribute("class", "link backtrack-link");
                
                const nodoAtras = document.getElementById(`node-${{paso.origen.replace('.', '')}}`);
                if (nodoAtras) nodoAtras.setAttribute("class", "node backtracked");
            }}
        }}
        
        btnNext.addEventListener("click", () => {{
            if (playingInterval) pausar();
            if (indexPasoActual < pasos.length - 1) {{
                indexPasoActual++;
                actualizarVisualizacion();
            }}
        }});
        
        btnPrev.addEventListener("click", () => {{
            if (playingInterval) pausar();
            if (indexPasoActual >= 0) {{
                indexPasoActual--;
                actualizarVisualizacion();
            }}
        }});
        
        btnReset.addEventListener("click", () => {{
            if (playingInterval) pausar();
            indexPasoActual = -1;
            actualizarVisualizacion();
        }});
        
        function pausar() {{
            clearInterval(playingInterval);
            playingInterval = null;
            btnPlay.textContent = "Reproducir ▶";
            btnPlay.className = "primary";
        }}
        
        function reproducir() {{
            const velocidad = parseInt(selectSpeed.value);
            btnPlay.textContent = "Pausar ⏸";
            btnPlay.className = "success";
            
            playingInterval = setInterval(() => {{
                if (indexPasoActual < pasos.length - 1) {{
                    indexPasoActual++;
                    actualizarVisualizacion();
                }} else {{
                    pausar();
                }}
            }}, velocidad);
        }}
        
        btnPlay.addEventListener("click", () => {{
            if (playingInterval) {{
                pausar();
            }} else {{
                if (indexPasoActual === pasos.length - 1) indexPasoActual = -1;
                reproducir();
            }}
        }});
        
        selectSpeed.addEventListener("change", () => {{
            if (playingInterval) {{
                pausar();
                reproducir();
            }}
        }});
        
        // Inicializar al cargar la página
        inicializarGrafo();
        aplicarFiltro();
    </script>
</body>
</html>
"""
    # Guardar archivo HTML en el mismo directorio donde se encuentra este script
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_html = os.path.join(dir_actual, "visualizacion_backtracking.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"\n[ÉXITO] Se generó el archivo de visualización interactiva: {ruta_html}")
    
    # Intentar abrir el navegador automáticamente
    print(f"Abriendo visualización en tu navegador: file://{ruta_html}")
    webbrowser.open(f"file://{ruta_html}")
