---
title: "Estimación Puntual: Momentos y Máxima Verosimilitud"
tags: [teoria, estadistica, estimacion, geometrica, poisson, gamma, mle]
tipo: teoria
---

# Estimación Puntual: Momentos y Máxima Verosimilitud

> [!abstract] ¿Qué resuelve?
> Responde la pregunta que quedó abierta al estimar $p$ de la Geométrica en [[Ejemplos y ejercicios]] y $\lambda$ de la Poisson: dado un parámetro desconocido y datos reales, ¿qué número concreto reporto como "mi mejor estimación", y por qué ese número y no otro? Esta nota resume el capítulo 6 de Devore ("Estimación puntual") en una guía operativa de dos métodos, con la misma receta de pasos siempre, aplicada a varias distribuciones de [[Teoría Distribuciones Base]].

> [!info] Fuente
> Devore, cap. 6 "Estimación puntual" — §6.1 (conceptos generales: insesgamiento, error estándar, censura) y §6.2 (método de momentos, máxima verosimilitud). Blitzstein & Hwang casi no cubre esto — es un libro de probabilidad, no de inferencia estadística.

---

## Capa 1 — Intuición

- **Método de momentos:** haz que el promedio de tus datos sea igual al promedio que la fórmula teórica predice, y despeja el parámetro de esa igualdad.
- **Máxima verosimilitud:** de todos los valores posibles del parámetro, elige el que hace más creíble — más "esperable" — que hayan salido justo los datos que observaste, y ningunos otros.

---

## Capa 2 — Ejemplo a mano

El caso más simple posible: de **20 clientes** que recibieron un cupón de bienvenida, **5 lo canjearon**. $X_i=1$ si canjeó, $0$ si no. $n=20$, $\sum x_i = 5$, $\bar x = 0.25$.

**Método de momentos.** El parámetro $p$ de una Bernoulli es exactamente $E[X]$, así que:
$$\bar x = p \;\Rightarrow\; \hat p_{MOM} = 0.25$$

**Máxima verosimilitud.** La probabilidad conjunta de ver 5 canjes y 15 no-canjes, con clientes independientes, es:
$$L(p) = p^{5}(1-p)^{15}$$

Prueba con lápiz y papel tres valores de $p$ y compara (en unidades de $10^{-5}$):

| $p$ | $L(p)=p^{5}(1-p)^{15}$ |
|---|---|
| 0.20 | $1.13$ |
| **0.25** | $\mathbf{1.30}$ |
| 0.30 | $1.15$ |

$p=0.25$ da el valor más alto — es el que hace más creíble haber observado justo 5 canjes de 20. Deriva $\ln L(p)=5\ln p+15\ln(1-p)$ e iguala a 0 y confirmas lo mismo por cálculo: $\hat p_{MLE}=5/20=0.25$.

Acá momentos y verosimilitud dieron el mismo número — pero eso **no es una regla general**, es solo lo que pasa en este caso particular. Los ejemplos de la Capa 3 muestran cuándo se mantiene y cuándo no.

---

## Capa 3 — Formalización

### La receta general

> [!note] Método de momentos (Devore §6.2)
> El **$k$-ésimo momento poblacional** es $E(X^k)$; el **$k$-ésimo momento muestral** es $\frac{1}{n}\sum X_i^k$. Con $m$ parámetros desconocidos, se igualan los primeros $m$ momentos muestrales a los primeros $m$ momentos poblacionales y se resuelve el sistema.

> [!note] Máxima verosimilitud (Devore §6.2)
> Dada la muestra $X_1,\dots,X_n$, la función de masa/densidad conjunta vista como función del parámetro $\theta$ (con los datos ya fijos) es la **función de verosimilitud** $L(\theta)$. El estimador $\hat\theta$ es el que la maximiza.
>
> Pasos: 1) $L(\theta)=\prod_i f(x_i;\theta)$ · 2) $\ln L(\theta)$ (el producto se vuelve suma) · 3) derivar e igualar a 0 · 4) despejar $\hat\theta$, o resolver numéricamente si no hay forma cerrada.

### La receta aplicada, distribución por distribución

**Poisson — tasa de compras $\lambda$.** Datos: compras mensuales de 5 clientes, $x=(2,3,1,4,0)$, $\bar x=2$.
$$\text{MOM: } E[X]=\lambda \;\Rightarrow\; \hat\lambda=\bar x=2 \qquad\qquad \text{MLE: } \ln L(\lambda)=-n\lambda+(\textstyle\sum x_i)\ln\lambda \;\Rightarrow\; \hat\lambda=\bar x=2$$

**Geométrica — recompras antes de abandonar $p$.** Datos: 5 clientes con recompras confirmadas, $x=(3,0,1,2,0)$, $\bar x=1.2$.
$$\text{MOM: } E[X]=\tfrac{1-p}{p} \;\Rightarrow\; \hat p=\tfrac{1}{1+1.2}\approx0.4545 \qquad \text{MLE: } \hat p=\tfrac{n}{n+\sum x_i}=\tfrac{5}{11}\approx0.4545$$

**Exponencial — días entre compras $\lambda$.** Datos: días entre compras consecutivas, $x=(12,8,15,5,10)$, $\bar x=10$.
$$\text{MOM: } E[X]=\tfrac{1}{\lambda} \;\Rightarrow\; \hat\lambda=\tfrac{1}{\bar x}=0.1 \qquad\qquad \text{MLE: } \hat\lambda=\tfrac{n}{\sum x_i}=\tfrac{5}{50}=0.1$$

En estos tres casos MOM y MLE vuelven a coincidir — pasa siempre que el único parámetro se pueda despejar directo de $E[X]$. El siguiente ejemplo rompe ese patrón.

**Gamma — cómo se reparten los ritmos $\lambda$ entre clientes.** Usando la notación de [[Teoría Distribuciones Base]], $\text{Gamma}(r,\alpha)$ con $E[X]=r/\alpha$, $E[X^2]=r(r+1)/\alpha^2$. Datos: ritmo individual (compras/mes) estimado de 6 clientes, $x=(0.5,\,1.2,\,0.8,\,2.1,\,1.5,\,0.9)$, $\bar x\approx1.1667$, $\frac{1}{n}\sum x_i^2\approx1.6333$.

$$\text{MOM: } \hat r = \frac{\bar x^2}{\frac1n\sum x_i^2-\bar x^2}\approx5.00 \qquad \hat\alpha=\frac{\hat r}{\bar x}\approx4.29$$

Para la **verosimilitud** no hay forma cerrada — al derivar $\ln L(r,\alpha)$ respecto a $r$ aparece la función digamma $\psi(r)$, que no se puede despejar a mano. Es el mismo tipo de obstáculo que Devore encuentra con Weibull (Ejemplo 6.19): la ecuación existe, pero se resuelve con un método numérico iterativo, no con álgebra. Esto es exactamente lo que hace la Capa 5.

> [!important] Cuándo se prefiere uno sobre el otro
> Con $n$ grande, el estimador de máxima verosimilitud es aproximadamente insesgado y tiene la varianza más pequeña posible entre todos los estimadores (Devore, p.249) — por eso, cuando MOM y MLE dan números distintos (como en Gamma), **se prefiere MLE**, aunque cueste más calcularlo.

### Censura — el paso que no puedes saltarte con datos reales

> [!warning] Recordatorio de la conversación
> Cuando armamos la cohorte de 5 clientes con regla de abandono a 3 meses, uno de ellos seguía comprando al cortar los datos — no cumplía la regla, pero tampoco sabías si la iba a cumplir después. Ese cliente se excluyó del cálculo. Devore formaliza esto en el Ejemplo 6.8 (p.237-238): en pruebas de vida útil, cortar el experimento antes de que **todos** los componentes fallen se llama *censura*; el estimador correcto usa solo los casos confirmados, ponderados por el tiempo total acumulado, y sigue siendo insesgado — tratar a los censurados como si ya hubieran terminado (o como si nunca fueran a terminar) sesga la estimación.

### Reportar el estimador: error estándar

Un número solo (ej. $\hat p=0.25$) no dice nada sobre su precisión. Devore recomienda siempre acompañarlo del **error estándar** — la desviación estándar del propio estimador. Para $\hat p=X/n$ de una Binomial, $\widehat\sigma_{\hat p}=\sqrt{\hat p(1-\hat p)/n}$; con fórmulas más complicadas (como Gamma), Devore usa **bootstrap** (Ejemplo 6.11): remuestrear los datos con reemplazo cientos de veces y tomar la desviación estándar de esas estimaciones repetidas.

---

## Capa 4 — Puente visual

Grafica $\ln L(p)$ contra $p$ entre 0 y 1 para el ejemplo del cupón: es una curva cóncava con un único pico exactamente en $p=0.25$. "Maximizar la verosimilitud" es, literalmente, encontrar la cima de esa montaña. El método de momentos no tiene esta imagen — es álgebra pura (igualar dos números y despejar), no una búsqueda de máximo.

---

## Capa 5 — Código

```python
import numpy as np
from scipy import stats, optimize
import matplotlib.pyplot as plt

# ---------- Bernoulli: canje de cupón (Capa 2) ----------
x_cupon = np.array([1]*5 + [0]*15)
p_mom = x_cupon.mean()
p_mle = x_cupon.sum() / len(x_cupon)          # misma fórmula acá
print(f"Bernoulli   -> MOM p̂={p_mom:.4f}  MLE p̂={p_mle:.4f}")

# ---------- Poisson: compras mensuales ----------
x_poisson = np.array([2, 3, 1, 4, 0])
lambda_hat = x_poisson.mean()                  # MOM = MLE = X̄
print(f"Poisson     -> λ̂={lambda_hat:.4f}")

# ---------- Geométrica: recompras antes de abandonar ----------
x_geom = np.array([3, 0, 1, 2, 0])
p_hat = 1 / (1 + x_geom.mean())
print(f"Geométrica  -> p̂={p_hat:.4f}")

# ---------- Exponencial: días entre compras ----------
x_expo = np.array([12, 8, 15, 5, 10])
lambda_a_mano = 1 / x_expo.mean()
_, scale_scipy = stats.expon.fit(x_expo, floc=0)   # scipy también resuelve el MLE
print(f"Exponencial -> λ̂ (a mano)={lambda_a_mano:.4f}  λ̂ (scipy)={1/scale_scipy:.4f}")

# ---------- Gamma: reparto de ritmos entre clientes ----------
x_gamma = np.array([0.5, 1.2, 0.8, 2.1, 1.5, 0.9])
x_bar, m2 = x_gamma.mean(), (x_gamma**2).mean()

r_mom = x_bar**2 / (m2 - x_bar**2)             # MOM: forma cerrada
alpha_mom = r_mom / x_bar
print(f"Gamma MOM   -> r̂={r_mom:.4f}  α̂={alpha_mom:.4f}")

def neg_log_lik(params):                        # MLE: sin forma cerrada, optimización numérica
    r, alpha = params
    if r <= 0 or alpha <= 0:
        return np.inf
    return -np.sum(stats.gamma.logpdf(x_gamma, a=r, scale=1/alpha))

resultado = optimize.minimize(neg_log_lik, x0=[r_mom, alpha_mom], method="Nelder-Mead")
r_mle, alpha_mle = resultado.x
print(f"Gamma MLE   -> r̂={r_mle:.4f}  α̂={alpha_mle:.4f}  (numérico)")

# ---------- Capa 4: la verosimilitud como una montaña (Bernoulli) ----------
p_grid = np.linspace(0.01, 0.99, 400)
log_L = x_cupon.sum() * np.log(p_grid) + (len(x_cupon) - x_cupon.sum()) * np.log(1 - p_grid)

plt.plot(p_grid, log_L)
plt.axvline(p_mle, linestyle="--", color="gray", label=f"p̂ = {p_mle:.2f}")
plt.xlabel("p"); plt.ylabel("ln L(p)")
plt.title("Log-verosimilitud del canje de cupón")
plt.legend(); plt.show()
```

Cada bloque traza de vuelta a la Capa 3: `.mean()` es siempre $\bar X$; las fórmulas de Poisson, Geométrica y Exponencial son las mismas que se despejaron a mano; `r_mom`/`alpha_mom` son las fórmulas cerradas de la Gamma; y `neg_log_lik` + `optimize.minimize` son la traducción directa de "no hay forma cerrada, resuélvelo numéricamente" — la negativa de $\ln L(r,\alpha)$ porque `minimize` busca mínimos, no máximos.

---

> [!important] Resumen operativo — pasos para estimar cualquier parámetro
> 1. Define qué parámetro quieres estimar y qué distribución supones que generó los datos.
> 2. Reúne las observaciones $x_1,\dots,x_n$. Si hay datos censurados (casos incompletos), sepáralos — no los trates como si el proceso ya hubiera terminado para ellos.
> 3. **Momentos:** iguala $\bar X$ (y momentos superiores si hay más de un parámetro) a las fórmulas teóricas $E[X]$, $E[X^2],\dots$ y despeja.
> 4. **Máxima verosimilitud:** escribe $L(\theta)=\prod f(x_i;\theta)$, toma $\ln$, deriva, iguala a 0, y despeja — si no se puede despejar a mano (Gamma, Weibull), resuelve numéricamente.
> 5. Cuando ambos den números distintos, prefiere MLE: es el que mejor se comporta con $n$ grande.
> 6. Reporta el estimador **junto con su error estándar** — nunca solo el número puntual.
