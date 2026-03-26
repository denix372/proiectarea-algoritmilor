# Recapitulare Examen PA: Algoritmi Aleatori

## 1. Quicksort Randomizat (Las Vegas)

**A) Ideea algoritmului:** Sortare prin divizarea vectorului în jurul unui pivot. Elementele mai mici merg la stânga, cele mai mari la dreapta. Eficiența depinde critic de cât de "echilibrată" este împărțirea.

**B) Partea randomizată:** Alegerea pivotului. În loc de o poziție fixă (ex: prima), selectăm un index `i = random(st, dr)` și îl interschimbăm cu elementul de control.

**C) Clasificare:** **Las Vegas**. Întoarce întotdeauna soluția corectă (vectorul sortat), dar timpul de execuție este o variabilă aleatoare.

**D) Mini-demonstrație complexitate:**
- **Recurența:** $T(n) = n + T(k) + T(n-k-1)$. În cazul cel mai rău (pivot extrem), $T(n) = O(n^2)$.
- **Pivotul "bun":** Un pivot este considerat "bun" dacă pică în intervalul central $[n/4, 3n/4]$. Probabilitatea este de $1/2$ (jumătate din elemente).
- **Impact:** Dacă alegem un pivot bun, dimensiunea subproblemelor scade la cel mult $3n/4$.
- **Analiza probabilistică:** Probabilitatea de a NU alege un pivot bun în $k$ pași este $(1/2)^k$. Aceasta scade exponențial.
- **Definiție PA:** Spunem că Quicksort are complexitatea $O(n \log n)$ cu probabilitate de cel puțin $1 - n^{-\alpha}$, deoarece adâncimea arborelui de recursie este limitată la $O(\log n)$ prin faptul că majoritatea pivotărilor vor fi "suficient de bune" într-un număr limitat de încercări.

**E) Esențial pentru examen:**
- Quicksort clasic are $O(n^2)$ pe date deja sortate. Randomizarea elimină corelația între ordinea datelor și performanță.
- Noțiunea de "High Probability" ($1 - n^{-\alpha}$): garantează că în practică nu vom vedea niciodată cazul $O(n^2)$.
- Pivotul median din 3: crește probabilitatea unui pivot bun de la $1/2$ la $11/16$ (sau valori similare), scăzând constanta din fața lui $n \log n$.

---

## 2. Miller-Rabin (Monte Carlo)

**A) Ideea algoritmului:** Verifică dacă un număr $n$ este prim folosind proprietăți de teoria numerelor (Mica Teoremă a lui Fermat și inexistența rădăcinilor pătrate netriviale ale lui 1 modulo $n$).

**B) Partea randomizată:** Alegerea bazei $a \in [2, n-2]$ pentru care se face verificarea.

**C) Clasificare:** **Monte Carlo**. Algoritmul poate returna "Prim" pentru un număr compus (eroare fals-pozitivă), dar dacă returnează "Compus", rezultatul este sigur corect.

**D) Mini-demonstrație complexitate:**
- **Martorii:** Un număr $a$ este "martor" dacă demonstrează că $n$ e compus. Teorema Miller-Rabin spune că pentru orice $n$ compus, cel puțin $3/4$ din baze sunt martori.
- **Probabilitatea de eroare:** La un singur test, probabilitatea ca un număr compus să treacă drept prim este $\le 1/4$.
- **Repetare:** După $k$ teste independente, probabilitatea de eroare scade la $(1/4)^k$.
- **Complexitate:** Un test implică o ridicare la putere modulară: $O(\log n)$ înmulțiri de numere mari. Total: $O(k \cdot \log^3 n)$.
- **Definiție PA:** Algoritmii Monte Carlo au complexitatea $O(g(n))$ dacă probabilitatea ca soluția să fie corectă este de cel puțin $1 - n^{-\alpha}$. Aici, alegând $k = \frac{\alpha}{2} \log_2 n$ teste, eroarea devine neglijabilă.

**E) Esențial pentru examen:**
- Diferența față de testul Fermat simplu: Fermat eșuează pe numerele Carmichael (ex: 561). Miller-Rabin funcționează deoarece verifică și dacă pe parcursul ridicării la putere apare $a^2 \equiv 1 \pmod n$ pentru $a \not\equiv \pm 1 \pmod n$.
- Este un algoritm de tip "probabilistic primality test": probabilitatea de eroare poate fi făcută mai mică decât probabilitatea unei erori hardware.

---

## 3. Algoritmul "Linia care se repetă" (Las Vegas)

**A) Ideea algoritmului:** Într-o secvență de $n$ linii, o anumită linie (titlul) apare de cel puțin $10\%$ ori ($q \ge 10\%$). Trebuie să o găsim rapid.

**B) Partea randomizată:** Alegerea a două indexuri aleatorii $i$ și $j$ din secvență și compararea liniilor corespunzătoare.

**C) Clasificare:** **Las Vegas**. Algoritmul rulează într-o buclă `while(true)` până când găsește două linii identice. Rezultatul este garantat corect, timpul este variabil.

**D) Mini-demonstrație complexitate:**
- **Probabilitatea de succes la un pas ($P_s$):** Probabilitatea ca atât $i$ cât și $j$ să indice linia repetată este $(\frac{r}{n}) \times (\frac{r-1}{n})$, unde $r$ este numărul de apariții. Deoarece $r = n \cdot q$, avem $P_s \approx q^2$. Pentru $q=0.1$, $P_s \approx 0.01$ (1%).
- **Probabilitatea de eșec după $m$ pași:** $P_f = (1 - P_s)^m$.
- **Complexitate:** Vrem ca $P_f \le n^{-\alpha}$. Aplicând logaritm: $m \cdot \ln(1 - P_s) \le -\alpha \ln n \Rightarrow m \approx O(\log n)$.
- **Intuție:** Deoarece avem o șansă constantă de succes la fiecare pas, numărul de pași urmați este o distribuție geometrică cu medie constantă.
- **Definiție PA:** Timpul de execuție este $O(\log n)$ cu o probabilitate de cel puțin $1 - n^{-\alpha}$.

**E) Esențial pentru examen:**
- Varianta deterministă ar fi $O(n^2)$ (comparații între toate perechile) sau $O(n \log n)$ cu sortare/hashing.
- Randomizarea reduce problema la un număr mic de eșantionări, profitând de ponderea mare (10%) a soluției în spațiul de căutare.
- Strategia: "Dacă un ac e mare într-un car cu fân, trage de câteva ori la întâmplare și îl vei găsi".

---

## 4. Hashing Polinomial (Monte Carlo / Las Vegas)

**A) Ideea algoritmului:** Conversia unui string într-un număr (hash) folosind o formulă polinomială: $H(s) = \sum s_i \cdot B^i \pmod M$. Permite compararea stringurilor în $O(1)$.

**B) Partea randomizată:** Alegerea bazei $B$ (adesea un număr prim) și uneori a modulo-ului $M$.

**C) Clasificare:** 
- **Monte Carlo:** Dacă decidem că două stringuri sunt egale doar pentru că au același hash (risc de coliziune).
- **Las Vegas:** Dacă la egalitatea hash-urilor facem și o verificare directă a stringurilor (timpul crește în caz de coliziune, dar rezultatul e cert).

**D) Mini-demonstrație complexitate:**
- **Probabilitatea de coliziune:** Pentru două stringuri diferite, probabilitatea ca $H(s_1) = H(s_2)$ este de aproximativ $1/M$ (dacă hash-ul e uniform).
- **Paradoxul Zilei de Naștere:** Dacă avem $N$ stringuri, probabilitatea unei coliziuni crește rapid când $N \approx \sqrt{M}$.
- **Complexitate (LV):** Timp mediu $O(1)$ pentru comparare. Dacă apare coliziune, $O(L)$ pentru verificare directă. Dacă $M$ este foarte mare ($10^9$ sau $10^{18}$), probabilitatea de coliziune pe date reale este infimă.
- **Definiție PA:** Eroarea (coliziunea) este $O(1/M)$. Putem atinge probabilitatea $1 - n^{-\alpha}$ folosind "Double Hashing" (două perechi diferite de $B$ și $M$).

**E) Esențial pentru examen:**
- Rolling Hash: Permite calculul hash-ului pentru o fereastră glisantă în $O(1)$ prin formula $H_{new} = (H_{old} - s_{out} \cdot B^{L-1}) \cdot B + s_{in} \pmod M$.
- Alegerea lui $B$ și $M$: $B >$ mărimea alfabetului, $M$ prim mare pentru a evita pattern-uri repetitive.
- Birthday Attack: Motivul pentru care $M = 2^{32}$ este nesigur (coliziuni la $\sim 65000$ stringuri), fiind preferat $M = 2^{61}-1$ (Mersenne prime) sau double hashing pe 32 biți.