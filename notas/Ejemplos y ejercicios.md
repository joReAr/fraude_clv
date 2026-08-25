---
title: "Ejemplos y ejercicios"
tags: [ejercicios, estadistica, poisson, geometrica, exponencial, gamma, beta]
tipo: ejercicios
---

# Ejemplos y ejercicios

Práctica de resolución manual, distribución por distribución. Definiciones y demostraciones completas están en [[Teoría Distribuciones Base]] — acá solo se recuerda la fórmula antes de usarla, y cada sección sigue el mismo patrón: un ejemplo sencillo, uno más complicado (con datos reales cuando aplica), y un ejercicio para resolver tú, con la verificación numérica escondida al final.

> [!info] Fuentes
> Ejemplos de Poisson inspirados en el "paradigma de Poisson" de Blitzstein & Hwang y en la aproximación Binomial→Poisson de Devore. Los ejemplos de Gamma usan la dualidad conteo-tiempo de Blitzstein & Hwang (cap. 5) para calcular probabilidades a mano vía la fórmula de Poisson. Ver [[Teoría Distribuciones Base]] para el detalle de cada fuente.

---

## Poisson

> [!note] Recordatorio
> $$P(X=k) = \frac{e^{-\mu}\,\mu^{k}}{k!}, \qquad \mu = \lambda\,T$$
>
> **Donde:** $\lambda$ es la tasa por unidad de tiempo, $T$ la duración observada, y $\mu$ el número medio de eventos esperado en ese periodo.

### Ejemplo 1 (sencillo) — visitas de un cliente en un mes

> [!example] Enunciado
> Una clienta de Metro visita la tienda a un ritmo constante de $\lambda = 2$ compras por mes. ¿Cuál es la probabilidad de que **este mes haga exactamente 3 compras**?

**Paso 1 — identificar los parámetros.**
Se observa un solo mes, así que $T = 1$. Con $\lambda = 2$:
$$\mu = \lambda\,T = 2 \times 1 = 2$$

**Paso 2 — plantear la fórmula con los valores conocidos.**
Se pide $P(X=3)$, o sea $k=3$:
$$P(X=3) = \frac{e^{-2}\,2^{3}}{3!}$$

**Paso 3 — calcular cada pieza por separado.**
$$e^{-2} \approx 0.1353 \qquad 2^{3} = 8 \qquad 3! = 3\times2\times1 = 6$$

**Paso 4 — combinar.**
$$P(X=3) = \frac{0.1353 \times 8}{6} = \frac{1.0827}{6} \approx 0.1804$$

**Paso 5 — interpretar.**
Hay **18.04%** de probabilidad de que la clienta compre exactamente 3 veces este mes. Coherente con la tabla de la Definición 2.1 en [[Teoría Distribuciones Base]] (misma $\mu=2$, mismo resultado): no es azar, es la misma cuenta.

### Ejemplo 2 (más complicado) — con datos reales del proyecto, dos meses y complemento

> [!example] Enunciado
> En `ecom_sinteticos.parquet`, el mes `202301` (enero 2023) tiene **37,526 transacciones** repartidas entre **27,013 clientes** distintos que compraron ese mes.
>
> Usamos esa razón como estimación de la tasa mensual de compra $\lambda$ de un cliente activo típico.
>
> a) Estima $\lambda$.
> b) Si esa tasa se mantiene constante e independiente durante **enero y febrero** (2 meses), ¿cuál es la probabilidad de que el cliente compre **exactamente 3 veces en total** en ese periodo?
> c) ¿Cuál es la probabilidad de que compre **al menos una vez** en esos 2 meses?

**Paso 1 — estimar $\lambda$ a partir de los datos.**
$$\lambda = \frac{\text{trx totales}}{\text{clientes activos}} = \frac{37526}{27013} \approx 1.39 \text{ compras/cliente-mes}$$

> [!warning] Cuidado con este $\lambda$
> Es la tasa **entre quienes ya compraron** ese mes — no incluye a los clientes que no compraron nada. Es un estimador sesgado al alza de la tasa "real" de toda la base, y asume que todos los clientes comparten el mismo $\lambda$ (equidispersión). Este es justo el supuesto que la Binomial Negativa relaja mezclando Poisson con Gamma — ver [[NBD - Poisson, Gamma y Binomial Negativa]].

**Paso 2 — pasar de 1 a 2 meses.**
Dos formas equivalentes de llegar al mismo $\mu$:
- Directo: $\mu = \lambda T = 1.39 \times 2 = 2.78$
- Vía aditividad (Proposición 2.4, demostrada en [[Teoría Distribuciones Base]] §2.2): si $X_{ene}\sim\text{Poisson}(\lambda)$ y $X_{feb}\sim\text{Poisson}(\lambda)$ son independientes con la misma tasa, $X_{ene}+X_{feb}\sim\text{Poisson}(\lambda+\lambda) = \text{Poisson}(2.78)$

$$\mu = 2.78$$

**Paso 3 — parte (b): $P(X=3)$ con $\mu=2.78$.**
$$P(X=3) = \frac{e^{-2.78}\,(2.78)^{3}}{3!}$$
$$e^{-2.78} \approx 0.0621 \qquad (2.78)^{3} \approx 21.485 \qquad 3! = 6$$
$$P(X=3) = \frac{0.0621 \times 21.485}{6} = \frac{1.3342}{6} \approx 0.2222$$

Probabilidad de **exactamente 3 compras en los 2 meses: 22.22%**.

**Paso 4 — parte (c): $P(X\geq 1)$ por complemento.**
Calcular "al menos una vez" directamente exigiría sumar $P(X=1)+P(X=2)+\dots$ hasta infinito. Es más simple usar el complemento de "ninguna vez":
$$P(X\geq 1) = 1 - P(X=0) = 1 - \frac{e^{-2.78}\,(2.78)^{0}}{0!} = 1 - e^{-2.78}$$
$$P(X\geq 1) = 1 - 0.0621 \approx 0.9379$$

Probabilidad de que compre **al menos una vez en los 2 meses: 93.79%**.

**Paso 5 — interpretar.**
Con esta tasa, casi seguro (94%) el cliente vuelve al menos una vez en dos meses, pero el resultado exacto "3 compras" tiene su propio peso (22%) — no está concentrado en un solo valor. Nota también que el complemento evitó sumar una serie infinita de términos.

### Ejemplo 3 (más complicado) — cuando Poisson aproxima a la Binomial

> [!example] Enunciado
> Una tienda lanza una oferta relámpago de 1 hora y envía la notificación a $n=4000$ clientes de la app. Cada cliente, independientemente de los demás, tiene una probabilidad muy baja $p=0.0008$ de comprar durante esa hora exacta (estimado de ofertas relámpago anteriores).
>
> a) Verifica que se puede aproximar por Poisson.
> b) ¿Cuál es la probabilidad de que **nadie** compre en esa hora?
> c) ¿Cuál es la probabilidad de que compren **3 o más** clientes?

Esto ya no es "un cliente con tasa $\lambda$" como en los Ejemplos 1 y 2 — es al revés: **muchos clientes ($n=4000$), cada uno con una probabilidad de "éxito" $p$ diminuta**. Es el paradigma de Poisson de la Proposición 2.5 en [[Teoría Distribuciones Base]] §2.3: técnicamente $X\sim\text{Binomial}(n,p)$, pero calcular eso a mano es impracticable ($4000!$ no se puede escribir), así que se aproxima por Poisson.

**Paso 1 — verificar la regla empírica.**
$$n = 4000 > 50 \qquad np = 4000\times0.0008 = 3.2 < 5$$
Se cumplen las dos condiciones de Devore — la aproximación es válida.

**Paso 2 — calcular $\mu = np$.**
$$\mu = 3.2$$

**Paso 3 — parte (b): $P(X=0)$.**
$$P(X=0) = \frac{e^{-3.2}\,3.2^{0}}{0!} = e^{-3.2} \approx 0.0408$$

Probabilidad de que **nadie compre en la hora: 4.08%** — baja, aunque cada cliente individualmente casi nunca compra: son 4000 oportunidades, y algunas suelen convertir.

**Paso 4 — parte (c): $P(X\geq 3)$ por complemento.**
Sumar de 3 a infinito es imposible a mano; se resta lo que falta hasta 2:
$$P(X\geq 3) = 1 - P(X=0) - P(X=1) - P(X=2)$$
$$P(X=1) = \frac{e^{-3.2}\,3.2^{1}}{1!} \approx 0.1304 \qquad P(X=2) = \frac{e^{-3.2}\,3.2^{2}}{2!} \approx 0.2087$$
$$P(X\geq 3) = 1 - 0.0408 - 0.1304 - 0.2087 \approx 0.6201$$

Probabilidad de que **compren 3 o más: 62.01%**.

**Paso 5 — interpretar y verificar.**
El valor binomial exacto de $P(X=0)$ es $0.04071$ y el de $P(X\geq3)$ es $0.62020$ — la aproximación Poisson (con 3 multiplicaciones) coincide con la Binomial exacta (que exigiría combinatoria sobre 4000 clientes) hasta el tercer decimal. Esta es la utilidad práctica de la Proposición 2.5: cuando $n$ es grande y $p$ chico, Poisson **reemplaza** a la Binomial sin perder precisión relevante.

### Ejercicio Poisson — para resolver tú

> [!example] Enunciado
> El mes `202303` (marzo 2023) del mismo dataset tiene **46,591 transacciones** entre **34,375 clientes** activos.
>
> a) Estima $\lambda_{marzo}$ (misma lógica que el Paso 1 del Ejemplo 2).
> b) Con $T=1$ mes, calcula $P(X=0)$ y $P(X=1)$ paso a paso.
> c) Usa el complemento para obtener $P(X\geq 2)$ a partir de lo anterior.
> d) Supón que esa tasa se mantiene constante durante **todo el primer trimestre** ($T=3$ meses, usando la misma idea de aditividad del Ejemplo 2). Calcula $\mu_{trimestre}$ y luego $P(X=4)$ para el trimestre completo.
> e) Ahora, como en el Ejemplo 3: supón (dato hipotético, no del dataset) que de los **34,375 clientes activos** de marzo, cada uno tiene independientemente una probabilidad muy baja $p=0.0001$ de hacer una devolución ese mismo día. Verifica la regla empírica, calcula $\mu$, y obtén $P(X=0)$ y $P(X\geq 5)$ devoluciones ese día.

Resuélvelo con el mismo desglose en pasos de los ejemplos (identificar $\mu$ → plantear la fórmula → calcular cada pieza → combinar → interpretar). Las partes (a)-(d) siguen la lógica del Ejemplo 2 (un cliente, tasa $\lambda$); la parte (e) sigue la lógica del Ejemplo 3 (muchos clientes, probabilidad $p$ pequeña cada uno). Cuando termines, revisamos juntos.

> [!note]- Verificación (solo resultados finales, sin desarrollo — ábrelo cuando ya hayas resuelto)
> $\lambda_{marzo} \approx 1.3554$
> $P(X=0) \approx 0.2579$
> $P(X=1) \approx 0.3495$
> $P(X\geq 2) \approx 0.3927$
> $\mu_{trimestre} \approx 4.0661$
> $P(X=4) \approx 0.1953$
> (e) $n=34375>50$, $np\approx3.4375<5$ ✓ · $\mu \approx 3.4375$ · $P(X=0) \approx 0.0321$ · $P(X\geq 5) \approx 0.2628$

---

## Geométrica

> [!note] Recordatorio
> $$P(X=k) = (1-p)^{k}\,p, \qquad E[X] = \frac{1-p}{p}, \qquad \text{Var}(X) = \frac{1-p}{p^{2}}$$
>
> **Donde:** $p$ es la probabilidad de abandono tras cada compra, y $X$ el número de recompras (fracasos en abandonar) antes de que ocurra.

### Ejemplo 1 (sencillo) — cuántas recompras antes de irse

> [!example] Enunciado
> En este local, tras cada compra, un cliente tiene una probabilidad $p=0.2$ de no volver (abandonar). ¿Cuál es la probabilidad de que haga **exactamente 4 recompras** antes de irse ($X=4$)?

**Paso 1 — identificar los parámetros.**
$p=0.2$ es la probabilidad de abandono ("éxito" en la convención de la fórmula). Se pide $k=4$ recompras (4 "fracasos" en abandonar, es decir, 4 veces que sigue comprando) antes del quinto intento, donde abandona.

**Paso 2 — plantear la fórmula.**
$$P(X=4) = (1-0.2)^{4}\times 0.2 = (0.8)^{4}\times 0.2$$

**Paso 3 — calcular cada pieza.**
$$0.8^{4} = 0.8\times0.8\times0.8\times0.8 = 0.4096$$

**Paso 4 — combinar.**
$$P(X=4) = 0.4096 \times 0.2 = 0.08192$$

**Paso 5 — interpretar.**
Hay **8.19%** de probabilidad de que el cliente haga exactamente 4 recompras y luego se vaya. Nota que, aunque este valor no es el más alto (el pico está en $X=0$, ver Ejemplo 3.3 de la teoría), sigue siendo un resultado concreto y calculable con la misma fórmula.

### Ejemplo 2 (más complicado) — con datos reales del proyecto y falta de memoria

> [!example] Enunciado
> En `ecom_sinteticos.parquet`, de los **27,013 clientes** que compraron en enero (`202301`), **17,210 no vuelven a comprar en febrero** (`202302`).
>
> Usamos esa proporción como una estimación cruda de la probabilidad **mensual** de abandono $p$.
>
> a) Estima $p$ (redondea a 2 decimales).
> b) Calcula el número esperado de recompras antes de que un cliente abandone, $E[X]$.
> c) Calcula $P(X=0)$, $P(X=1)$ y $P(X\geq 2)$.
> d) Un cliente ya hizo **3 recompras seguidas** (sigue activo). Usando la falta de memoria (Proposición 3.4), ¿cuál es la probabilidad de que haga **al menos 2 recompras más**?

**Paso 1 — estimar $p$.**
$$p = \frac{17210}{27013} \approx 0.6371 \approx 0.64$$

> [!warning] Cuidado con este $p$
> Es un abandono definido como "no compró el mes inmediatamente siguiente" — un criterio mucho más estricto que el usado en producción (`limite_recencia = 4 meses`, ver [[Diagnostico del modelo en produccion]]). Por eso da un valor tan alto: muchos de estos clientes probablemente vuelven más adelante, solo que no en febrero. Es una cota cruda, no la tasa de fuga real del negocio.

**Paso 2 — parte (b): valor esperado.**
$$E[X] = \frac{1-p}{p} = \frac{1-0.64}{0.64} = \frac{0.36}{0.64} = 0.5625 \text{ recompras}$$

Muy bajo — coherente con la sobredispersión que ya vimos en Poisson: hay muchísimos compradores de una sola vez.

**Paso 3 — parte (c): la distribución completa.**
$$P(X=0) = p = 0.64$$
$$P(X=1) = (1-p)\,p = 0.36\times0.64 = 0.2304$$
$$P(X\geq 2) = 1 - P(X=0) - P(X=1) = 1 - 0.64 - 0.2304 = 0.1296$$

**Paso 4 — parte (d): falta de memoria.**
Primero, la probabilidad de haber sobrevivido 3 rondas:
$$P(X\geq 3) = (1-p)^{3} = 0.36^{3} \approx 0.0467$$

Por la Proposición 3.4, $P(X\geq 3+2 \mid X\geq 3) = P(X\geq 2)$ — la probabilidad condicional de 2 recompras más es **exactamente la misma** que la probabilidad incondicional de que cualquier cliente nuevo haga 2 recompras:
$$P(X\geq 2) = (1-p)^{2} = 0.36^{2} = 0.1296$$

**Paso 5 — interpretar.**
Que el cliente ya lleve 3 recompras **no lo acerca ni lo aleja** de irse: su probabilidad de aguantar 2 rondas más (12.96%) es idéntica a la de un cliente que recién empieza. Es la misma idea que viste en la Exponencial (§4 de la teoría) — acá aplicada al conteo, no al tiempo.

### Ejercicio Geométrica — para resolver tú

> [!example] Enunciado
> Supón un segmento de clientes con probabilidad de abandono $p=0.5$ tras cada compra.
>
> a) Calcula $P(X=0)$, $P(X=1)$ y $P(X\geq 2)$.
> b) Calcula $E[X]$ y $\text{Var}(X)$.
> c) Un cliente ya recompró **2 veces**. Usando la falta de memoria, ¿cuál es la probabilidad de que recompre **al menos 1 vez más**? (Pista: por la Proposición 3.4, esto debe coincidir con una probabilidad incondicional que ya calculaste en (a) o puedes calcular directo.)

Sigue el mismo desglose en pasos de los ejemplos. Cuando termines, revisamos juntos.

> [!note]- Verificación (solo resultados finales — ábrelo cuando ya hayas resuelto)
> $P(X=0) = 0.5$
> $P(X=1) = 0.25$
> $P(X\geq 2) = 0.25$
> $E[X] = 1.0$
> $\text{Var}(X) = 2.0$
> (c) $P(X\geq 1) = 0.5$ (igual a la probabilidad incondicional de al menos 1 recompra)

---

## Exponencial

> [!note] Recordatorio
> $$f(w) = \lambda\,e^{-\lambda w}, \qquad P(W>w) = e^{-\lambda w}, \qquad E[W] = \frac{1}{\lambda}$$
>
> **Donde:** $\lambda$ debe estar en la **misma unidad de tiempo** que $w$ — si $\lambda$ está en compras/mes y preguntas por días, conviértelo primero.

### Ejemplo 1 (sencillo) — cuánto falta para la próxima compra

> [!example] Enunciado
> Una clienta compra a un ritmo constante de $\lambda=2$ compras al mes (la misma clienta del Ejemplo 1 de Poisson). ¿Cuál es la probabilidad de que **pasen más de 20 días** antes de su próxima compra?

**Paso 1 — igualar unidades.**
$\lambda$ está en compras/mes pero la pregunta es en días. Un mes ≈ 30 días:
$$\lambda = \frac{2}{30} \approx 0.0667 \text{ por día}$$

**Paso 2 — plantear la fórmula.**
$$P(W>20) = e^{-\lambda \times 20} = e^{-0.0667\times20}$$

**Paso 3 — calcular el exponente.**
$$0.0667\times20 \approx 1.333$$

**Paso 4 — evaluar.**
$$P(W>20) = e^{-1.333} \approx 0.2636$$

**Paso 5 — interpretar.**
Hay **26.36%** de probabilidad de que la clienta tarde más de 20 días en volver a comprar. Nota la conexión con Poisson: "más de 20 días sin comprar" es exactamente lo mismo que "cero compras en esos 20 días", y por eso esta cuenta usa la misma $\lambda$ que ya usaste en la Definición 2.1.

### Ejemplo 2 (más complicado) — con datos reales, falta de memoria y mediana

> [!example] Enunciado
> Usando la tasa real estimada en el Ejemplo 2 de Poisson, $\lambda=1.39$ compras/mes:
>
> a) ¿Cuál es la probabilidad de que pasen **más de 45 días** antes de la próxima compra?
> b) Dado que ya pasaron **20 días sin comprar**, ¿cuál es la probabilidad de que pasen **al menos 45 días en total**? Usa la falta de memoria (Proposición 4.2).
> c) ¿Cuál es la **mediana** del tiempo entre compras? Compárala con la media $E[W]$.

**Paso 1 — convertir $\lambda$ a días.**
$$\lambda = \frac{1.39}{30} \approx 0.04633 \text{ por día}$$

**Paso 2 — parte (a).**
$$P(W>45) = e^{-0.04633\times45} = e^{-2.085} \approx 0.1243$$

**Paso 3 — parte (b): falta de memoria.**
La pregunta "¿al menos 45 días en total, dado que ya van 20?" es $P(W>20+25 \mid W>20)$. Por la Proposición 4.2, esto es igual a $P(W>25)$ — el tiempo ya esperado **no cuenta**:
$$P(W>25) = e^{-0.04633\times25} = e^{-1.158} \approx 0.3140$$

El cliente no "está más cerca" de comprar por haber esperado ya 20 días — su espera restante se ve exactamente igual a si empezara de cero.

**Paso 4 — parte (c): mediana.**
Se busca $w$ tal que $P(W\leq w) = 0.5$, es decir $1-e^{-\lambda w}=0.5 \Rightarrow e^{-\lambda w}=0.5$. Despejando:
$$w = \frac{\ln 2}{\lambda} = \frac{0.6931}{0.04633} \approx 14.96 \text{ días}$$

**Paso 5 — interpretar.**
La media es $E[W]=1/\lambda\approx21.58$ días, pero la **mediana es 14.96** — bastante menor. Es el mismo patrón asimétrico que ya viste con la Gamma ($r<1$) en la teoría: la mayoría de las esperas son cortas, pero unas pocas esperas largas jalan el promedio hacia arriba. La razón mediana/media siempre es $\ln 2\approx0.693$ en la Exponencial, sin importar $\lambda$.

### Ejercicio Exponencial — para resolver tú

> [!example] Enunciado
> Usa la tasa real de marzo, $\lambda_{marzo}\approx1.3554$ compras/mes (la misma del ejercicio de Poisson).
>
> a) Convierte $\lambda$ a una tasa diaria.
> b) Calcula $P(W>30 \text{ días})$.
> c) Calcula $P(W>60 \text{ días})$.
> d) Verifica numéricamente la falta de memoria: calcula $P(W>60 \mid W>30)$ dividiendo tus resultados de (b) y (c), y confirma que coincide con $P(W>30)$.
> e) Calcula la mediana del tiempo entre compras.

Sigue el mismo desglose en pasos del Ejemplo 2. Cuando termines, revisamos juntos.

> [!note]- Verificación (solo resultados finales — ábrelo cuando ya hayas resuelto)
> $\lambda \approx 0.04518$ por día
> $P(W>30) \approx 0.2578$
> $P(W>60) \approx 0.0665$
> (d) $P(W>60)/P(W>30) \approx 0.2578$ — coincide con $P(W>30)$ ✓
> mediana $\approx 15.34$ días

---

## Gamma

> [!note] Recordatorio
> $$f(\lambda) = \frac{\alpha^{r}}{\Gamma(r)}\,\lambda^{r-1}e^{-\alpha\lambda}, \qquad E[\lambda] = \frac{r}{\alpha}$$
>
> **Herramienta clave para calcular a mano** (dualidad conteo-tiempo, Blitzstein & Hwang): si $T\sim\text{Gamma}(r,\alpha)$ con $r$ entero es el tiempo hasta el $r$-ésimo evento de un proceso de Poisson de tasa $\alpha$, entonces "el $r$-ésimo evento todavía no llegó en el tiempo $t$" es lo mismo que "hubo menos de $r$ eventos en $[0,t]$":
> $$P(T>t) = P(\text{Poisson}(\alpha t) < r) = \sum_{k=0}^{r-1}\frac{e^{-\alpha t}(\alpha t)^{k}}{k!}$$
>
> Esto convierte una probabilidad Gamma (que en general exige la función gamma incompleta) en una suma finita de términos de Poisson — la misma fórmula que ya dominas.

### Ejemplo 1 (sencillo) — tiempo hasta la 3ª compra, vía dualidad con Poisson

> [!example] Enunciado
> Un cliente compra a un ritmo $\lambda=2$ compras al mes (acá $\alpha=\lambda=2$/mes, en notación Gamma).
>
> a) ¿Cuántos días **en promedio** tarda en hacer su 3ª compra?
> b) ¿Cuál es la probabilidad de que la 3ª compra tarde **más de 60 días**?

**Paso 1 — identificar los parámetros.**
Se espera el 3er evento, así que $r=3$. La tasa en días es $\alpha = 2/30 \approx 0.0667$/día.

**Paso 2 — parte (a): media.**
$$E[T] = \frac{r}{\alpha} = \frac{3}{2/30} = 45 \text{ días}$$

**Paso 3 — parte (b): plantear la dualidad.**
"La 3ª compra tarda más de 60 días" es lo mismo que "hubo menos de 3 compras en los primeros 60 días", un conteo Poisson con $\alpha t = 0.0667\times60 = 4$:
$$P(T>60) = P(\text{Poisson}(4) < 3) = P(N{=}0)+P(N{=}1)+P(N{=}2)$$

**Paso 4 — calcular cada término (misma fórmula de Poisson de siempre).**
$$e^{-4}\approx0.0183 \qquad P(N{=}0)=0.0183 \qquad P(N{=}1)=0.0183\times4=0.0733 \qquad P(N{=}2)=\frac{0.0183\times16}{2}=0.1465$$

**Paso 5 — sumar e interpretar.**
$$P(T>60) = 0.0183+0.0733+0.1465 \approx 0.2381$$

Aunque en promedio la 3ª compra llega a los 45 días, hay casi **24% de probabilidad** de que tarde más de 60 — la Gamma tiene cola larga, igual que la Exponencial que la compone.

### Ejemplo 2 (más complicado) — la Gamma como repartidor de tasas, con dos métodos

> [!example] Enunciado
> Supón que el ritmo de compra $\lambda$ de los clientes de una categoría se reparte $\text{Gamma}(r=2,\alpha=0.1)$ por año.
>
> a) ¿Cuál es el ritmo medio de la base?
> b) ¿Qué proporción de clientes tiene un ritmo **menor a 10 compras al año**, $P(\lambda<10)$? Resuélvelo de dos formas: derivando la CDF a mano vía integración por partes, y verificando con la dualidad de Poisson.

**Paso 1 — parte (a): media.**
$$E[\lambda] = \frac{r}{\alpha} = \frac{2}{0.1} = 20 \text{ compras/año}$$

**Paso 2 — parte (b), método 1: integrar por partes.**
Con $r=2$, la densidad es $f(x)=\alpha^{2}x\,e^{-\alpha x}$. Se integra por partes con $u=x$, $dv=\alpha^2e^{-\alpha x}dx$ (entonces $du=dx$, $v=-\alpha e^{-\alpha x}$):
$$F(x) = \int_0^x \alpha^2 t\,e^{-\alpha t}\,dt = \Big[-\alpha t\,e^{-\alpha t}\Big]_0^x + \int_0^x \alpha e^{-\alpha t}dt = -\alpha x e^{-\alpha x} + \Big[-e^{-\alpha t}\Big]_0^x$$
$$F(x) = 1 - e^{-\alpha x}(1+\alpha x)$$

**Paso 3 — evaluar en $x=10$.**
Con $\alpha=0.1$, $\alpha x = 1$:
$$F(10) = 1 - e^{-1}(1+1) = 1-2e^{-1} = 1 - 2(0.3679) = 1-0.7358 = 0.2642$$

**Paso 4 — método 2: verificar con la dualidad de Poisson.**
"$\lambda<10$" equivale a "ya ocurrieron 2 o más eventos en un proceso de Poisson observado durante $x=10$ con tasa $\alpha=0.1$", es decir $\alpha x=1$:
$$P(\lambda<10) = P(\text{Poisson}(1)\geq2) = 1-P(N{=}0)-P(N{=}1) = 1-e^{-1}-e^{-1} = 1-2e^{-1} \approx 0.2642$$

Los dos métodos coinciden exactamente — no es casualidad, son la misma dualidad conteo-tiempo vista desde dos ángulos.

**Paso 5 — interpretar.**
26.42% de la base tiene un ritmo menor a 10/año, aunque la media es 20 — otra vez el patrón: con $r$ pequeño, buena parte de la base queda **por debajo** del promedio (mismo fenómeno que el Ejemplo 5.3 de la teoría, con otros parámetros).

### Ejercicio Gamma — para resolver tú

> [!example] Enunciado
> Un cliente compra a un ritmo $\lambda=3$ compras al mes.
>
> a) ¿Cuál es el número esperado de días hasta su **4ª compra**?
> b) Usando la dualidad con Poisson, calcula la probabilidad de que la 4ª compra tarde **más de 50 días**.
>
> Aparte, supón que el ritmo de compra de una categoría de clientes se reparte $\text{Gamma}(r=3,\alpha=0.15)$ por año.
>
> c) Calcula el ritmo medio de la base.
> d) Calcula $P(\lambda<10)$ usando la CDF de Erlang-3 (dada como ayuda, se deriva igual que en el Ejemplo 2 pero integrando por partes dos veces):
> $$F(x) = 1 - e^{-\alpha x}\left(1+\alpha x+\frac{(\alpha x)^{2}}{2}\right)$$

Sigue el mismo desglose en pasos de los ejemplos. Cuando termines, revisamos juntos.

> [!note]- Verificación (solo resultados finales — ábrelo cuando ya hayas resuelto)
> (a) $E[T] = 40$ días
> (b) $\alpha t = 5$ · $P(T>50) = P(\text{Poisson}(5)<4) \approx 0.2650$
> (c) $E[\lambda] = 20$/año
> (d) $\alpha x = 1.5$ · $P(\lambda<10) \approx 0.1912$

---

## Beta

> [!note] Recordatorio
> $$f(p) = \frac{p^{a-1}(1-p)^{b-1}}{B(a,b)}, \qquad E[p] = \frac{a}{a+b}$$
>
> Cuando $a,b$ son enteros pequeños, la densidad es un **polinomio** en $p$ y su integral se puede hacer a mano (igual que Devore hace en su ejemplo PERT). Recordatorio de conjugación (§6.3 de la teoría): la posterior tras observar $k$ éxitos en $n$ ensayos es $\text{Beta}(a+k,\ b+n-k)$.

### Ejemplo 1 (sencillo) — probabilidad de abandono con Beta(2,3)

> [!example] Enunciado
> Se estima que la probabilidad de abandono $p$ de un cliente cualquiera de esta categoría sigue $\text{Beta}(a=2,b=3)$ (el mismo prior del Ejemplo 7.3 de la teoría).
>
> a) ¿Cuál es la probabilidad media de abandono en la base?
> b) ¿Cuál es la probabilidad de que un cliente elegido al azar tenga $p<0.5$?

**Paso 1 — parte (a): media.**
$$E[p] = \frac{a}{a+b} = \frac{2}{5} = 0.4$$

**Paso 2 — construir la densidad.**
$$B(2,3) = \frac{\Gamma(2)\Gamma(3)}{\Gamma(5)} = \frac{1!\times2!}{4!} = \frac{2}{24} = \frac{1}{12} \quad\Rightarrow\quad f(p) = 12\,p(1-p)^{2}$$

**Paso 3 — expandir el polinomio e integrar.**
$$12p(1-p)^2 = 12p - 24p^2 + 12p^3 \quad\Rightarrow\quad F(x) = 6x^2 - 8x^3 + 3x^4$$

**Paso 4 — evaluar en $x=0.5$.**
$$F(0.5) = 6(0.25) - 8(0.125) + 3(0.0625) = 1.5 - 1 + 0.1875 = 0.6875$$

**Paso 5 — interpretar.**
**68.75%** de los clientes tiene $p<0.5$, aunque el promedio de la base es 0.4 — el mismo patrón asimétrico que ya viste en Gamma: la mayoría cae por debajo del promedio.

### Ejemplo 2 (más complicado) — conjugación y encogimiento con integración a mano

> [!example] Enunciado
> Un prior $\text{Beta}(a=1,b=3)$ refleja la creencia de que la tasa de canje de un cupón ronda 25% ($E[p]=1/4$). Se envía el cupón a $n=2$ clientes y se observa $k=1$ canje.
>
> a) Calcula la posterior.
> b) Calcula $E[p]$ posterior y compáralo con la tasa cruda $k/n$.
> c) Calcula $P(p<0.5)$ bajo la posterior, integrando la densidad a mano.

**Paso 1 — parte (a): actualizar con la regla de conjugación.**
$$\text{Beta}(a+k,\ b+n-k) = \text{Beta}(1+1,\ 3+2-1) = \text{Beta}(2,4)$$

**Paso 2 — parte (b): media posterior vs. tasa cruda.**
$$E[p] = \frac{2}{2+4} = \frac{1}{3} \approx 0.333 \qquad\text{vs.}\qquad \frac{k}{n} = \frac{1}{2} = 0.5$$

Con solo 2 clientes, el prior todavía pesa: la estimación se modera de 0.5 a 0.333, hacia la creencia inicial (0.25) — el mismo encogimiento de §6.4/§7.2 de la teoría, ahora con la cuenta completa a la vista.

**Paso 3 — parte (c): construir la densidad posterior.**
$$B(2,4) = \frac{\Gamma(2)\Gamma(4)}{\Gamma(6)} = \frac{1!\times3!}{5!} = \frac{6}{120} = \frac{1}{20} \quad\Rightarrow\quad f(p) = 20\,p(1-p)^{3}$$

**Paso 4 — expandir e integrar.**
$$20p(1-p)^3 = 20p - 60p^2 + 60p^3 - 20p^4 \quad\Rightarrow\quad F(x) = 10x^2 - 20x^3 + 15x^4 - 4x^5$$

**Paso 5 — evaluar en $x=0.5$ e interpretar.**
$$F(0.5) = 10(0.25) - 20(0.125) + 15(0.0625) - 4(0.03125) = 2.5-2.5+0.9375-0.125 = 0.8125$$

**81.25%** de probabilidad posterior de que $p<0.5$ — consistente con que la posterior está centrada en 0.333, lejos de 0.5.

### Ejercicio Beta — para resolver tú

> [!example] Enunciado
> Un prior $\text{Beta}(a=1,b=2)$ (media $1/3$) refleja la creencia inicial sobre la tasa de conversión de una campaña. Se envía a $n=3$ clientes y se observan $k=2$ conversiones.
>
> a) Calcula la posterior.
> b) Calcula $E[p]$ posterior y compáralo con la tasa cruda $k/n$.
> c) Calcula $P(p<0.3)$ bajo la posterior, integrando a mano (igual que en el Ejemplo 2).
> d) Sin integrar: la posterior que obtuviste en (a), ¿tiene alguna simetría que te permita saber $P(p<0.5)$ a simple vista? Verifica tu razonamiento con el valor exacto.

Sigue el mismo desglose en pasos del Ejemplo 2. Cuando termines, revisamos juntos.

> [!note]- Verificación (solo resultados finales — ábrelo cuando ya hayas resuelto)
> (a) posterior $= \text{Beta}(3,3)$
> (b) $E[p] = 0.5$ vs. tasa cruda $k/n \approx 0.667$
> (c) $P(p<0.3) \approx 0.1631$
> (d) $\text{Beta}(3,3)$ es simétrica respecto a $0.5$ (mismos $a=b$) ⟹ $P(p<0.5) = 0.5$ exacto, sin integrar
