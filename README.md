 Descripción general del proyecto 
La página web "Curiosidades Espaciales" es una aplicación interactiva diseñada 
para entusiastas del espacio que desean aprender datos interesantes sobre el 
universo. Utilizando el framework Reflex en Python, hemos creado una interfaz 
moderna con las siguientes características adicionales: 
• Diseño responsive que se adapta a dispositivos móviles y desktop 
• Efectos visuales sutiles en las tarjetas (hover effects) 
• Sistema de categorización para futuras expansiones (planetas, estrellas, 
galaxias) 
• Optimización de imágenes para carga rápida 
• Validación de enlaces externos para garantizar fuentes confiables 

2. Buenas prácticas aplicadas - Separación clara entre estado (State) y presentación (index()). - Reutilización de componentes (rx.card, rx.vstack, rx.hstack). - Uso de variables reactivas para manejar interactividad (State.cantidad). - Código legible, comentado y modular. - Estilo visual consistente, limpio y moderno. - Datos organizados en una lista curiosidades[] que se puede expandir fácilmente - También en accesibilidad Texto alternativo para todas las imágenes - Contraste de colores WCAG AA compliant 
- Navegación mediante teclado

  
3. Requisitos del parcial cubiertos 
Requisito 
Uso obligatorio del framework Reflex 
Página con tema libre y diseño sencillo 
Código documentado 
Subido a GitHub 
Desplegado en la nube (Reflex)

 
4. Crea un repositorio nuevo en https://github.com 
- En tu terminal: 
-cd parcial_2 
-git init 
-git add . 
-git commit -m "parcial_2" 
-git remote add origin https://github.com/timcito/parcial_2.git 
-git push -u origin main


5. Cómo desplegar gratis con Reflex 
1. Ejecuta: reflex export 
2. Se creará una carpeta out/ 
3. Ve a https://reflex.dev/ / y crea un sitio 
4. Arrastra la carpeta out/ al área de subida 
5. Reflex te dará un enlace como: https://parcial-2-lime-wood.reflex.run/
- Enlaces requeridos - Repositorio GitHub: https://github.com/timcito/parcial_2 - Página web desplegada: https://parcial-2-lime-wood.reflex.run/ 
