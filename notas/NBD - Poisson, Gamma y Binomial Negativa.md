---
title: "La distribución binomial negativa como mezcla Poisson-Gamma"
tags: [teoria, estadistica, btyd, nbd, poisson, gamma]
tipo: teoria
---

# La distribución binomial negativa como mezcla Poisson-Gamma

> [!abstract] Resultado central
> Si el número de eventos de cada individuo sigue un Poisson, y las tasas individuales se reparten en la población según una Gamma, entonces el conteo observado en un individuo elegido al azar sigue una **binomial negativa**.
>
> La NBD no se postula: **se deduce**.

Nota teórica. Ejemplos con valores genéricos. Los hallazgos sobre datos reales están en [[Descubrimientos - ecommerce metro]].

---

## 1 · Planteamiento

Se quiere describir cuántas veces compra un cliente en un periodo.

El primer modelo natural es el Poisson: un solo parámetro, la tasa media. Pero impone una restricción muy fuerte —varianza igual a la media— que los datos de compra casi nunca cumplen: siempre hay más dispersión de la que el Poisson admite. A ese exceso se le llama **sobredispersión**.

La causa no suele ser que el proceso individual no sea Poisson. Es que **la población no es homogénea**: no existe "el cliente promedio", existen clientes con ritmos muy distintos. La sección 4 lo demuestra con un ejemplo mínimo.

La solución es no fijar una tasa, sino una *distribución de tasas*.

---

## 2 · Los dos ladrillos

### 2.1 · Poisson: el conteo de un individuo

> [!note] Definición
> $X$ sigue una distribución de Poisson de media $\mu$ si
> $$P(X = k) = \frac{e^{-\mu}\mu^{k}}{k!}, \qquad k = 0, 1, 2, \dots$$
> Si los eventos ocurren a tasa $\lambda$ durante un tiempo $T$, entonces $\mu = \lambda T$.

> [!note] Propiedad
> $$E[X] = \text{Var}(X) = \mu$$
> Media y varianza coinciden. **Esta igualdad es la que falla en la práctica.**

> [!example] Ejemplo 2.1
> Un cliente compra a razón de $\lambda = 2$ veces al año. Observado durante $T = 1$ año, $\mu = 2$:
>
> | $k$ | 0 | 1 | 2 | 3 | 4 |
> |---|---|---|---|---|---|
> | $P(X=k)$ | 0.1353 | 0.2707 | 0.2707 | 0.1804 | 0.0902 |
>
> La cola se apaga rápido: $P(X \geq 10) = 0.000046$, aproximadamente 1 de cada 22,000.

### 2.2 · Gamma: el reparto de las tasas

> [!note] Definición
> $\lambda$ sigue una distribución Gamma de forma $r > 0$ y escala inversa $\alpha > 0$ si
> $$f(\lambda) = \frac{\alpha^{r}}{\Gamma(r)}\lambda^{r-1}e^{-\alpha\lambda}, \qquad \lambda > 0$$
> con $E[\lambda] = r/\alpha$ y $\text{Var}(\lambda) = r/\alpha^{2}$.

Se elige la Gamma por tres razones: solo toma valores positivos (una tasa nunca es negativa), su forma es flexible, y —la decisiva— es **conjugada del Poisson**, lo que hace que la mezcla tenga solución cerrada.

> [!important] El papel de $r$
> - $r > 1$: densidad con forma de campana asimétrica, población relativamente homogénea
> - $r = 1$: exponencial
> - $r < 1$: densidad en forma de **"L"**, infinita cerca de cero y con cola larga
>
> $r < 1$ describe una población muy dispar: mucha masa de individuos casi inactivos y una minoría intensa. Cuanto **menor** es $r$, **mayor** la heterogeneidad.

> [!example] Ejemplo 2.2
> Con $r = 0.5$ y $\alpha = 0.25$ (tiempo en años), la tasa media es $r/\alpha = 2$ compras al año. Pero la distribución es muy asimétrica:
>
> | percentil | 25 | 50 | 75 | 90 |
> |---|---|---|---|---|
> | $\lambda$ | 0.203 | 0.910 | 2.647 | 5.411 |
>
> La media (2.0) más que duplica a la mediana (0.91). El promedio está dominado por una minoría de tasa alta — el "cliente promedio" no representa a nadie.

---

## 3 · La mezcla

No se observa el $\lambda$ de ningún individuo. Lo que se observa es el conteo promediado sobre todos los $\lambda$ posibles, ponderado por su densidad.

> [!important] Proposición 3.1
> Sea $X \mid \lambda \sim \text{Poisson}(\lambda T)$ y $\lambda \sim \text{Gamma}(r, \alpha)$. Entonces
> $$P(X = x) = \frac{\Gamma(r+x)}{\Gamma(r)\,x!}\left(\frac{\alpha}{\alpha+T}\right)^{r}\left(\frac{T}{\alpha+T}\right)^{x}$$
> es decir, $X \sim \text{BN}(r,\ p)$ con $\;p = \dfrac{\alpha}{\alpha+T}$.

> [!note]- Demostración
> Por la ley de probabilidad total,
> $$P(X = x) = \int_{0}^{\infty} \frac{e^{-\lambda T}(\lambda T)^{x}}{x!}\cdot\frac{\alpha^{r}}{\Gamma(r)}\lambda^{r-1}e^{-\alpha\lambda}\,d\lambda$$
> Se extraen del integrando las constantes respecto de $\lambda$ y se agrupan las potencias y exponenciales:
> $$= \frac{T^{x}\alpha^{r}}{x!\,\Gamma(r)}\int_{0}^{\infty}\lambda^{r+x-1}e^{-(\alpha+T)\lambda}\,d\lambda$$
> El integrando es el núcleo de una $\text{Gamma}(r+x,\ \alpha+T)$, cuya integral vale $\Gamma(r+x)/(\alpha+T)^{r+x}$:
> $$= \frac{T^{x}\alpha^{r}}{x!\,\Gamma(r)}\cdot\frac{\Gamma(r+x)}{(\alpha+T)^{r+x}}$$
> Reagrupando $(\alpha+T)^{r+x} = (\alpha+T)^{r}(\alpha+T)^{x}$ se obtiene la expresión del enunciado. $\blacksquare$

> [!warning] Observación 3.2 — el parámetro $p$ depende del individuo
> $p = \alpha/(\alpha+T)$ **es función de $T$**, el tiempo durante el que se observó a ese individuo.
>
> Si todos se observan el mismo tiempo, $p$ es una constante y se recupera la binomial negativa de los libros de texto. Si los individuos tienen historias de distinta longitud —lo habitual con clientes captados en momentos distintos— **hay un $p$ por individuo**.
>
> Ignorarlo obliga al modelo a explicar con un único $p$ a individuos observados durante 20 días y durante 1,300. Es la causa más frecuente de que el ajuste no converja.

### Media y varianza

> [!important] Corolario 3.3
> $$E[X] = \frac{rT}{\alpha}, \qquad \text{Var}(X) = \underbrace{\frac{rT}{\alpha}}_{\text{azar del conteo}} + \underbrace{\frac{rT^{2}}{\alpha^{2}}}_{\text{heterogeneidad}}$$

> [!note]- Demostración
> Por la ley de esperanza total, $E[X] = E[E[X\mid\lambda]] = E[\lambda T] = rT/\alpha$.
>
> Por la ley de varianza total,
> $$\text{Var}(X) = \underbrace{E[\text{Var}(X\mid\lambda)]}_{E[\lambda T] \;=\; rT/\alpha} + \underbrace{\text{Var}(E[X\mid\lambda])}_{T^{2}\text{Var}(\lambda) \;=\; rT^{2}/\alpha^{2}} \qquad \blacksquare$$

La varianza se parte en dos sumandos con significados distintos: el primero es el azar del proceso Poisson; el segundo, la dispersión de las tasas. **La varianza siempre supera a la media**, y el exceso mide exactamente cuánta heterogeneidad hay.

---

## 4 · Por qué mezclar genera sobredispersión

Este ejemplo aísla el mecanismo sin necesidad de la Gamma.

> [!example] Ejemplo 4.1
> Una población con dos tipos de individuos en partes iguales: la mitad con $\lambda = 0.5$, la mitad con $\lambda = 6$. Cada individuo es Poisson puro. Se observa $T = 1$.
>
> **Media**, por esperanza total:
> $$E[X] = \tfrac{1}{2}(0.5) + \tfrac{1}{2}(6) = 3.25$$
>
> **Varianza**, por varianza total. Como cada tipo es Poisson, $\text{Var}(X\mid\lambda) = \lambda$:
> $$E[\text{Var}(X\mid\lambda)] = 3.25$$
> $$E[\lambda^{2}] = \tfrac{0.25 + 36}{2} = 18.125 \;\Longrightarrow\; \text{Var}(E[X\mid\lambda]) = 18.125 - 3.25^{2} = 7.5625$$
> $$\text{Var}(X) = 3.25 + 7.5625 = 10.8125$$
>
> $$\frac{\text{Var}(X)}{E[X]} = 3.33$$

> [!success] Conclusión
> Sin alterar el supuesto Poisson de ningún individuo, el cociente pasó de 1.00 a 3.33 **solo por mezclar dos tipos**.
>
> La sobredispersión no significa que el proceso individual no sea Poisson. Significa que **se están promediando individuos distintos**. La Gamma es la versión continua de este mismo mecanismo.

---

## 5 · Comparación con el Poisson

> [!example] Ejemplo 5.1
> Se fija $r = 0.5$ y media 2, lo que da $p = 0.2$. Contra un Poisson de la **misma media**:
>
> | $k$ | Poisson | BN | razón |
> |---|---|---|---|
> | 0 | 0.1353 | **0.4472** | 3.3× |
> | 1 | 0.2707 | 0.1789 | 0.66× |
> | 2 | 0.2707 | 0.1073 | 0.40× |
> | 3 | 0.1804 | 0.0716 | 0.40× |
> | 4 | 0.0902 | 0.0501 | 0.56× |
>
> | | Poisson | BN |
> |---|---|---|
> | media | 2.0 | 2.0 |
> | varianza | 2.0 | **10.0** |
> | $P(X \geq 10)$ | 0.000046 | **0.036905** |
>
> La cola es **794 veces** más probable bajo la binomial negativa.

> [!success] La firma de una mezcla
> Con idéntica media, la BN pone **más masa en cero** y **más masa en la cola**, vaciando el centro.
>
> Tiene sentido: los individuos de tasa baja engordan el cero, los de tasa alta engordan la cola, y nadie queda en el medio. Un histograma con esa forma —pico en cero, valle, cola larga— es señal de heterogeneidad, no de un proceso raro.

---

## 6 · Estimación

### 6.1 · Método de los momentos

Sirve como punto de partida. Igualando media y varianza muestrales a las teóricas con $T$ constante:

$$\hat{r} = \frac{m^{2}}{v - m}, \qquad \hat{p} = \frac{m}{v}$$

donde $m$ y $v$ son media y varianza muestrales. Requiere $v > m$; si no se cumple, la binomial negativa no es el modelo adecuado.

> [!warning] Restricción
> Estas fórmulas suponen que **todos los individuos se observaron el mismo tiempo**. Con $T$ variable solo valen como semilla del optimizador, y hay que reescalar $\alpha$ usando $E[X] = rT/\alpha$:
> $$\hat{\alpha} = \frac{\hat{r}\,\bar{T}}{m}$$

### 6.2 · Máxima verosimilitud

$$\ell(r,\alpha) = \sum_{i=1}^{n}\left[\ln\Gamma(r+x_i) - \ln\Gamma(r) - \ln\Gamma(x_i+1) + r\ln\frac{\alpha}{\alpha+T_i} + x_i\ln\frac{T_i}{\alpha+T_i}\right]$$

> [!tip] Tres detalles de implementación
> **Reparametrizar.** Optimizar en $\log r$ y $\log\alpha$ en lugar de $r$ y $\alpha$. El optimizador recorre todo $\mathbb{R}$ mientras los parámetros permanecen positivos. Sin esto, un método sin restricciones propone valores negativos, la verosimilitud devuelve `NaN` y el ajuste colapsa.
>
> **Usar `gammaln`,** no el logaritmo de `gamma`. Evita desbordamiento.
>
> **Proteger el caso $x_i = 0$ con $T_i = 0$.** El término $x\ln T$ es $0\cdot\ln 0$; debe definirse como 0.

> [!warning] Sobre truncar en cero
> Es tentador descartar a los individuos con conteo cero y ajustar una binomial negativa truncada. **Casi siempre es un error.**
>
> La masa en cero es la que identifica $r$: sin ella el modelo cree que todos son activos y sobreestima la tasa. Un conteo de cero es un dato observado, no un dato faltante.
>
> Con $T$ en el modelo, un cero con $T$ pequeña se explica de forma natural, y la truncación deja de tener motivo.

---

## 7 · Interpretación bayesiana

La conjugación Gamma-Poisson da el posterior de un individuo concreto sin ningún cálculo adicional.

> [!important] Proposición 7.1
> $$\lambda_i \mid x_i, T_i \;\sim\; \text{Gamma}(r + x_i,\ \alpha + T_i), \qquad E[\lambda_i \mid x_i, T_i] = \frac{r + x_i}{\alpha + T_i}$$

La lectura es directa: **$r$ y $\alpha$ funcionan como eventos y tiempo imaginarios** que aporta la población. Un individuo sin historia hereda el prior; uno con mucha historia lo domina.

De ahí sale la predicción individual:

$$E[\text{eventos en los próximos } t \text{ periodos}] = \frac{r+x_i}{\alpha+T_i}\cdot t$$

> [!example] Ejemplo 7.2
> Con $r = 0.5$, $\alpha = 100$ días, dos individuos con **el mismo conteo** $x = 1$:
>
> | $T$ | $E[\lambda]$ (día) | $E[\lambda]$ (año) |
> |---|---|---|
> | 30 días | $1.5/130 = 0.01154$ | 4.21 |
> | 1000 días | $1.5/1100 = 0.00136$ | 0.50 |
>
> Ocho veces de diferencia. Un evento en el primer mes indica una tasa alta; un evento en tres años, una tasa baja. Un modelo sin $T$ los trataría igual.

---

## 8 · Límite del modelo

> [!warning] La NBD supone que el individuo nunca deja de estar activo
> Proyecta la tasa estimada hacia adelante indefinidamente. En contextos donde los individuos abandonan —que es el caso de cualquier cliente— esto **sobreestima sistemáticamente** la actividad futura.
>
> La NBD no contiene el concepto de abandono, así que ningún reajuste de $r$ y $\alpha$ lo corrige. Hace falta añadir un segundo proceso → [[BG-NBD y Pareto-NBD]].

---

## Resumen

| Símbolo | Significado |
|---|---|
| $\lambda$ | tasa de eventos de un individuo |
| $r$ | forma de la Gamma; **menor $r$ = más heterogeneidad** |
| $\alpha$ | escala de la Gamma, en unidades de tiempo |
| $T$ | tiempo durante el que se observó al individuo |
| $x$ | eventos observados |
| $p = \alpha/(\alpha+T)$ | parámetro de la BN, **propio de cada individuo** |
| $r/\alpha$ | tasa media de la población |

| Idea | |
|---|---|
| 1 | La NBD se deduce de mezclar Poisson con Gamma |
| 2 | La sobredispersión revela heterogeneidad, no un fallo del Poisson |
| 3 | $\text{Var} = $ azar $+$ heterogeneidad |
| 4 | $p$ depende de $T$: un valor por individuo |
| 5 | El posterior es $\text{Gamma}(r+x,\ \alpha+T)$ |

**Enlaces:** [[BG-NBD y Pareto-NBD]] · [[Descubrimientos - ecommerce metro]]
