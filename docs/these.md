```
2015-ENST-00xx
```
##### EDITE - ED 130

**Doctorat ParisTech**

**T H È S E**

```
pour obtenir le grade de docteur délivré par
```
**TÉLÉCOM ParisTech**

### Spécialité « Electronique et Communications »

```
présentée et soutenue publiquement par
```
### Gaël Kamdem De Teyou

```
le 31 Août 2015
```
**Calibration aveugle et adaptative des convertisseurs**

**analogique-numérique entrelacés temporellement**

```
Directeur de thèse : Patrick LOUMEAU
Co-encadrement de la thèse : Hervé PETIT
```
**Jury**

**M. Philippe Benabes** ,Professeur, Supélec, Gif sur Yvette Président

**M. Dominique DALLET** ,Professeur, ENSEIRB, Bordeaux Rapporteur
**M. Dominique MORCHE** ,Directeur de Recherche, CEA-Leti, Grenoble Rapporteur

**M. Stéphane PAQUELET** ,Responsable de Laboratoire, B-COM, Rennes Examinateur
**M. Patrick LOUMEAU** ,Professeur, Télécom ParisTech, Paris Directeur de thèse

**M. Hervé PETIT** ,Maitre de Conférences, Télécom ParisTech, Paris Co-Directeur de thèse

```
TÉLÉCOM ParisTech
école de l’Institut Mines-Télécom - membre de ParisTech
46 rue Barrault 75013 Paris - (+33) 1 45 81 77 77 - http://www.telecom-paristech.fr
```


Adaptive and Blind Background Calibration of

Channel Mismatches in Time-Interleaved ADCs

#### Gaël Kamdem De Teyou

#### September 23, 2015


# Acknowledgment

Several persons have supported me during this PhD research. First of all, I
would like to thank deeply my supervisors, Patrick Loumeau and Hervé Petit
for their openness, guidance and support during the course of this work. I am
also grateful to Renesas Design France which funded this research and where
I had the opportunity to work during my PhD. Especially, I want to thank
warmly Stephane Paquelet and Yann Le Guillou of Renesas who initiated this
work and who help me to understand the basics of ADCs.

My sincere thanks are due, to Philippe Benabes, Dominique Dallet and Do-
minique Morche members of this jury, for their availability and who accepted
to examine this work during summer.

I am extremely thankful to Hussein Fakhoury and Chadi Jabbour of Télécom
ParisTech for useful discussions and comments during this work. Also thanks
to my friends and colleagues at Télécom ParisTech for the fun we had together.

Special thanks go to my fiancée Lorie, for her patience, encouragement, and
support throughout my research. My brothers Harold, Maxime and Jordan
for their moral support. Above all, I would like to thank my parents for a
never-ending support and for all they did for me.



```
Abstract
```
Wireless receivers for emerging Software Define Radio require faster and
more accurate converters. A popular way to achieve this is by designing Time-
Interleaved ADCs (TI-ADCs). First low speed and high resolution sub-ADCs
are built, then they are interleaved, working alternatively as if they were a
single ADC but working at a much higher rate. TI-ADCs have emerged as a
good way to provide high speed data converters from relatively slow circuits.
However, unfortunately in this kind of architecture, new errors emerge and give
rise to nonlinear distortion which significantly degrade the resolution of the
overall TI-ADC. These errors come from discrepancies between the individual
sub-ADCs in the system and are commonly referred to as channel mismatch
errors. They consist of gain, time-skew, bandwidth and offset mismatch errors
and they should be mitigated.

There are two possible ways to deal with channel mismatches. The first is
to complexify the analog circuit design of the ADC in order to reduce the mag-
nitude of the original mismatches at the cost of more power consumption and
area. But this increases the time-to-market of the ADC. The second solution is
to alleviate the design and to correct the errors with a calibration technique.

In this work, a new digital blind calibration technique is proposed for TI-
ADCs which is able to correct the gain, time-skew, bandwidth and offset mis-
matches. The technique can be divided into two independent steps. The first
step is estimation and it consists in identifying the mismatches from the mea-
surements. In this step we use a rational fractional delay and a low-pass filter to
estimate adaptively the different mismatches. The second step is the compen-
sation which consists in reducing the errors due to channel mismatches. This
stage is based on the development of a matrix approach to find the suitable
filters to apply at the output of different channels.

This technique was tested on 14 bits ADCs from Analog Devices and the
results show the effectiveness of the technique.


## Contents



   - 0.1 Introduction
   - 0.2 Modèles d’erreurs dans les CANs
   - 0.3 Modèles de bruit dans les CANs
   - 0.4 Modèles d’erreurs dans les CANETs
   - 0.5 Calibration des CANETs
   - 0.6 Conclusion
- 1 Introduction
   - 1.1 Background and Motivation
   - 1.2 High Speed ADCs Design Challenges
   - 1.3 Time-Interleaved ADCs
   - 1.4 Related work on TI-ADCs
   - 1.5 Goal, Contribution and Thesis Organization
- 2 Analysis of Analogue to Digital Converters
   - 2.1 ADC Performance Specifications
      - 2.1.1 DC Accuracy
      - 2.1.2 Dynamic Performances
   - 2.2 Analysis of a Basic CMOS Sample and Hold
      - 2.2.1 Time-skew
      - 2.2.2 Bandwidth limitation
      - 2.2.3 Signal dependency of the on-resistance
      - 2.2.4 Charge Injection and Clock Feedthrough
   - 2.3 Others Sample and Hold architectures
      - 2.3.1 Close loop S/H
      - 2.3.2 Switched Capacitor S/H
      - 2.3.3 Double Sampling S/H
   - 2.4 Quantization
      - 2.4.1 Flash Architecture
      - 2.4.2 Successive Approximations Architecture
      - 2.4.3 Pipelined Architecture
      - 2.4.4 Delta-Sigma Architecture
      - 2.4.5 Summary on quantization architecture
   - 2.5 Summary and mathematical model at the ADC output
   - 2.6 Chapter conclusion
- 3 Noise modeling in ADCs
   - 3.1 Introduction
   - 3.2 Signal model
   - 3.3 Quantization Noise
      - 3.3.1 Total power
      - 3.3.2 Probability Density Function
      - 3.3.3 Power Spectral Density
   - 3.4 Thermal noise
      - 3.4.1 Probability Density Function
      - 3.4.2 Power Spectral Density
   - 3.5 Jitter Noise
      - 3.5.1 Signal to Noise Ratio
      - 3.5.2 Composition of jitter
      - 3.5.3 Aperture jitter
      - 3.5.4 Clock jitter
   - 3.6 Flicker Noise
   - 3.7 Conclusion
- 4 Time-Interleaved ADCs modeling
   - 4.1 Introduction
   - 4.2 Time Interleaved ADCs Architecture
      - 4.2.1 Clock
      - 4.2.2 Phase generator
      - 4.2.3 Buffers
   - 4.3 Time Domain Analysis
   - 4.4 Frequency domain representation
   - 4.5 Pairing between mismatches
      - 4.5.1 Spur power analysis
      - 4.5.2 Dynamic specifications of TI-ADCs
   - 4.6 Probabilistic Description of Mismatches
      - 4.6.1 Motivation
      - 4.6.2 Probability Density Function of SFDR and THD
      - 4.6.3 Cumulative Density Function of SFDR
   - 4.7 Integral and Differential Non-Linearities
   - 4.8 Conclusion
- 5 Proposed Digital Calibration Scheme
   - 5.1 Introduction and State of art
   - 5.2 Estimation of channel mismatches
   - 5.3 Compensation of channel mismatch errors
      - 5.3.1 Particular case M=2
      - 5.3.2 Before calibration
      - 5.3.3 After calibration
   - 5.4 Simulation results with a two-channel ADCs
   - 5.5 Impact of the signal bandwidth
   - 5.6 Measurement results on two-channel ADC board
   - 5.7 ASIC synthesis
   - 5.8 Conclusion
- 6 Conclusion and Perspectives
- Bibliography
- List of Figures
- List of Tables
   - cuit A Appendix A: CMOS Bootstrapped and Sample and Hold Cir-
      - CMOS Bootstrap circuit A.1 On-resistance in function of the input signal in a single ended
   - A.2 Output signal of a single ended bootstrap S/H circuit
      - A.2.1 Sampling mode
      - A.2.2 Hold mode
      - A.2.3 Homogeneous ODE
   - A.3 Solution of the inhomogeneous equation
   - A.4 Output of the S/H without nonlinearities
- B Spectrum of the TI-ADCs
   - B.1 Spectrum of the DC Component
   - B.2 Spectrum of the AC component
- C Statistical Analysis of TI-ADCs
   - C.1 Probability Density Function of Sa ( k )
   - C.2 PDF of Smax
   - C.3 Cumulative Density Function of Sa ( k )
- D Appendix E: Thermal Noise
      - D.0.1 Total power
      - D.0.2 Power spectral density of thermal noise
- E Power Spectral Density of Jitter
   - E.1 Useful property of WSS signal
   - E.2 Autocorrelation function of jitter noise
   - E.3 PSD of aperture jitter
   - E.4 PSD of sampling noise due to clock jitter of a free-running oscillator



# Notations

#### Symbols

For all this report, we use the following symbols.

**Symbol Explanation**

_q_ Quantization step, also called Least Significant Bit

_M_ Number of time interleaved ADC

_N_ Resolution of the ADC

_m_ Index identifying the _mth_ ADC

_fs_ Sampling frequency of the TI-ADCs

```
fs
M Sampling frequency of an individual ADC
```
_T s_ Sampling period of the TI-ADCs

_Gm_ Gain of the _mth_ ADC

_Om_ Offset of the _mth_ ADC

_ξ_ [ _n_ ] Jitter of the ADC at the instant _nTs_

_τms_ Time Skew of the _mth_ ADC

_hm_ ( _t_ ) Impulse response of the _mth_ ADC

_IN Lm_ ( _i_ ) Integral Non-Linearity of code _i_ of the _mth_ ADC

_DN Lm_ ( _i_ ) Differential Non-Linearity of code _i_ of the _mth_ ADC.


#### Abbreviations

For all this report, we use the following abbreviations.

**Abbreviation Explanation**

ADC Analog to Digital Converter

DTFT Discrete Time Fourier Transform

ENOB Effective Number Of Bits

PLL Phase Locked Loop

PDF Probability Density Function

PSD Power Spectral Density

SC Switched Capacitor

SDR Software Defined Radio

SFDR Spurious Free Dynamic Range

S/H Sample and Hold

SNDR Signal to Noise and Distortion Ratio

SNR Signal to Noise Ratio

TI-ADCs Time Interleaved Analog to Digital Converters

THD Total Harmonic Distortion


# French Summary

### 0.1 Introduction

Il y a une augmentation permanente du débit de données dans les standards de
communication sans fil. C’est ainsi qu’on est passé de 14.4 Kbits/s en 2G pour
atteindre 384 Kbits/s en 3G, puis 1 Gbits/s en 4G et plusieurs Gbits/s sont
attendus en 5G bien qu’elle ne soit pas encore standardisée. Ceci a été rendu
possible grâce à un certain nombre d’opérations sur la couche physique parmi
lesquelles l’augmentation de la largeur de bande. C’est ainsi qu’on est passé de
200 KHz par porteuse en 2G pour pouvoir atteindre dans certains cas 100 MHz
en 4G grâce à l’agrégation de porteuses, c’est-à-dire une largeur de bande 500
fois plus élevée qu’en 2G. Cette augmentation de la largeur de bande nécessite
des Convertisseurs Analogique-Numérique (CAN) plus rapides car le signal doit
être échantillonné au niveau du récepteur à au mois deux fois la largeur de bande.

Pour assurer la mobilité de l’usager afin qu’il puisse se connecter partout, le
terminal doit intégrer plusieurs bandes et les anciens standards doivent coexister
avec les nouveaux. Ceci constitue un gros challenge au niveau de l’architecture
de récepteur. La Fig. 1 par exemple illustre l’architecture d’un récepteur su-
perhétérodyne conventionnel. Il y a une partie de la RF qui est partagée puis
il y a une chaine de réception spécifique à chaque canal. Ainsi la complexité
d’un tel récepteur en termes de coût matériel augmente drastiquement avec le
nombre de standards et de canaux. La solution pour régler ce problème est la
radio logicielle (Software Defined Radio). Elle comprend une chaine de récep-
tion principalement réalisée en numérique (logiciel) et dans une moindre mesure
en matériel. La même infrastructure matérielle peut alors être réutilisée pour
les différents standards mais avec cette fois-ci un logiciel qui est spécifique au
standard et au service souhaité. Ceci est rendu possible en déplaçant le CAN
autant que possible vers l’antenne de façon à échantillonner le signal le plus tôt
possible et effectuer le reste de traitements dédiés en numérique comme le mon-
tre la Fig. 2. Cependant déplacer le convertisseur vers l’antenne augmente les
contraintes sur celui-ci qui doit être plus rapide tout en conservant une bonne
résolution.


```
Antenna
```
Preselection Filter

##### LNA IRF

```
Channel selection
Filter
```
##### ADC

##### ADC

##### I

##### Q

##### DSP

##### LO

```
Shared One receiver per channel
```
##### IF

```
LO Baseband
```
```
Figure 1: Architecture d’un récepteur superheterodyne conventionnel.
```
```
Filter
```
##### LNA

```
Wideband
```
##### ADC

##### DSP

```
Shared One DSP per channel
```
```
Figure 2: Radio logicielle idéale.
```

La Fig. 3 montre un état de l’art des CAN sur les 18 dernières années. Nous
avons représenté les CAN à approximations successives qui sont très appréciés
pour leur bonne résolution et leur faible consommation en puissance. Nous
pouvons remarquer que dans l’ensemble leur fréquence d’échantillonnage est
limitée à la centaine de mégahertz. Si nous visons des vitesses d’échantillonnage
supérieures comme par exemple 230 MHz pour le LTE-A il faudrait une autre
solution. On peut envisager les Convertisseurs Analogique-Numérique à En-
trelacement Temporel (CANET) qui ont une vitesse d’échantillonnage qui va de
la centaine de mégahertz à quelques gigahertz. Cependant on remarque que les
CANETs ont une résolution qui est plus faible que celle des CAN autonomes.
Ceci est du au fait que l’entrelacement introduit d’autres erreurs qui n’étaient
pas présentes dans les CAN autonomes. Ces erreurs proviennent des dispar-
ités entre les différents CAN et sont communément appelés « mismatchs ». On
distingue principalement les mismatchs de gain, time-skew, bande et offset qui
doivent être corrigés à travers une calibration.

```
Figure 3: Stand alone ADCs performance survey from 1997 to 2015.
```
La Fig. 4 montre l’architecture d’un CANET qui est constitué de plusieurs
CAN qui fonctionnent alternativement l’un après l’autre et l’ensemble se com-
porte comme un CAN unique mais qui a une fréquence d’échantillonnage M fois
supérieure à celle d’un CAN de chaque voie. Ce type d’architecture est util-
isé dans les applications comme les communications sans fil, l’instrumentation,
l’aérospatial et les stations de base pour le militaire. Comme avantage nous
avons la vitesse et comme inconvénient il y a l’apparition de nouvelles erreurs
appelées mismatchs qu’il faut calibrer.

On peut classer les techniques de calibration en plusieurs types suivant le
mode d’opération et l’emplacement de la correction. Il existe les calibrations


##### ADC 0

##### ADCM − 1

##### MUX

##### S/H 0

##### S/HM − 1

```
x ( t ) y[n]
```
```
Figure 4: Time Interleaved ADCs architecture.
```
différées dans lesquelles un signal de test connu est injecté à l’entrée du conver-
tisseur puis le signal de sortie est mesuré puis comparé au signal de l’entrée. Ceci
permet l’identification des mismatchs et la correction des erreurs. Ce type de
méthodes est adapté pour les applications comme l’instrumentation et la mesure
où on peut envisager une phase de diagnostique permettant de calibrer le con-
vertisseur puis une phase de fonctionnement où le CAN marche normalement.
Les méthodes de calibration différées ne sont pas adaptées pour les applications
temps réel comme les communications où le convertisseur doit toujours être en
cours de fonctionnement. La solution alternative est d’utiliser les méthodes en
ligne où la calibration opère en toile de fond tandis que le CAN fonctionne. Les
méthodes de calibration en ligne sont basées sur des techniques aveugles pour
estimer les mismatchs. En réalité l’estimation n’est jamais totalement aveugle
car on connait tout de même quelques informations statistiques sur le signal
comme sa densité spectrale de puissance et sa puissance totale. Si la correc-
tion utilise une rebouclage analogique sur le front-end du CAN on qualifie la
calibration de mixte. Les méthodes mixtes permettent d’obtenir de très forts
niveau de correction mais elles augmentent le temps de conception du circuit
car il faut modifier le circuit électronique du convertisseur. L’alternative est
d’utiliser les méthodes totalement numériques dans lesquelles la correction est
effectuée à l’aide d’un circuit numérique. Dans cette thèse nous intéresserons
aux calibrations en ligne et totalement numériques.

Le gain, le time-skew et l’offset ont été largement explorés mais le mismatch
de bande n’a été analysé que tout récemment. De plus La plupart des techniques
de calibration du mismatch de bande ne prennent pas en compte les mismatch
de gain et de time-skew. En effet les erreurs dues au mismatch de bande peu-
vent se combiner de façon constructive ou destructive avec les erreurs dues aux
mismatch de gain et de time-skew comme nous allons le démontrer dans cette
thèse. Donc par souci d’optimalité il faudrait traiter ces trois mismatchs en
même temps.


Cette thèse a deux volets. Le premier c’est un volet modélisation où nous
proposons des modèles qui permettent d’analyser les erreurs dans les CAN au-
tonomes. Nous aurons une attention spéciale sur la modélisation de la non-
linéarité dans les Echantillonneur/Bloqueur (E/B) bootstrappés, puis suivrons
les modèles de bruits dans les CAN et les modèles d’erreurs dans les structures
entrelacées. Le second volet consiste en méthode de calibration des mismatchs
de gain, time-skew et bande dans les CANETs. L’estimation se fait en aveu-
gle, de façon adaptative et est basée sur un filtrage passe-bas combiné avec
un filtre à retard fractionnaire. La compensation des erreurs est basée sur le
développement d’une approche matricielle pour réduire l’effet des mismatchs.

### 0.2 Modèles d’erreurs dans les CANs

La principale erreur analysée dans ce chapitre est la nonlinéarité de l’E/B. Un
E/B doit vérifier un certain nombre de contraintes parmi lesquelles les con-
traintes de consommation en puissance, de vitesse, de nonlinéarité et de dy-
namique de signal d’entrée. Parmi ces contraintes là, la contrainte de non-
linéarité est difficile à atteindre car de par sa structure de base l’E/B est non
linéaire. En effet la résistance de transistor-commutateur est donnée par la re-
lation (1) qui dépend de la tension grille-source qui elle-même dépend du signal
d’entrée. Cette dépendance de la tension grille-source avec le signal d’entrée
crée des nonlinéarités dans le circuit qui distordent le signal.

```
Ron =
```
##### 1

```
μCoxWL ( Vgs − Vth − Vds 2 )
```
##### (1)

La technique la plus populaire pour corriger cette nonlinéarité est de modifier
le circuit de l’E/B et de rajouter un circuit dit « Bootstrap » comme le montre
la Fig. 6. Des simulations en 65nm CMOS montrent que le montage du boot-
strap n’est pas suffisant car la résistance de transistor-commutateur continue de
varier avec le signal d’entrée. Cependant on peut noter que la variation devient
linéaire avec le signal d’entrée comme le montre la Fig. 5. Pour une variation
linéaire de la résistance avec le signal d’entrée et en considérant une capacité
de maintien idéale on démontre que le signal de sortie se compose d’un offset
à la fréquence 0, du signal fondamental et d’une harmonique de second ordre.
L’harmonique 2 étant l’harmonique dominante, elle peut être supprimée grâce
à une structure différentielle. Cependant les mismatchs entre les deux voies
de la structure différentielle limitent la correction et il est possible d’exprimer
l’harmonique 2 résiduelle en fonction du niveau de mismatch.

Les mismatchs étant aléatoires, nous faisons également une étude statistique
de cette distorsion. Cette étude nous permet d’obtenir la densité de proba-
bilité de la distorsion et de trouver de combien il faut réduire les mismatchs
pour obtenir une distorsion seuil avec un niveau de confiance spécifique. Pour
avoir une distorsion de l’ordre de 100 dB avec un niveau de confiance de 99.9 % il


```
0 0.2 0.4 0.6 0.8 1 1.
105
```
```
110
```
```
115
```
```
120
```
```
125
```
```
130
```
```
135
```
```
Input signal in V
```
##### R

```
on
```
```
in
```
##### Ω

Figure 5: Simulation results of the on-resistance of a bootstrapped S/H as a
function of the input signal in 65 nm CMOS process with supply voltage of
_vdd_ = 1_._ 2 V.

##### C

##### -

```
r r
```
```
r
r
```
```
r
r
```
```
r r r r
```
```
vdd
```
##### Φ Φ

##### Φ

##### Φ

##### Φ

##### M 1

##### N 1

##### C 3

```
c
x ( t )
```
```
y[n]
c
```
```
Figure 6: Logical structure of the bootstrap circuit.
```

faudrait que les mismatch soient plus petits que 1 %. Ceci fournit au concepteur
analogique des outils pour dimensionner son circuit et atteindre spécifications
technique désirées.

Il est à noter que les imperfections comme la nonlinéarité sont spécifiques
à chaque CAN et doivent être corrigées. En les corrigeant on obtient un CAN
linéaire dont le modèle mathématique est donné par les formules (2) et (3) où on
distingue une composante de filtrage, une composante d’offet et une composante
de bruit.

```
y [ n ] = yAC [ n ] + yDC [ n ] + vnoise [ n ] =
```
##### (

```
h ( p ,. ) ⋆ x
```
##### )

```
( nTs ) + O + vnoise [ n ] (2)
```
```
Y ( f ) = YAC ( f ) + YDC ( f )
```
```
= fs
```
##### +∑∞

```
k =−∞
```
##### {

```
H ( p ,. ) X (. ) + Oδ (. )
```
##### }∣∣

##### ∣

```
f − kfs
```
##### (3)

Ce modèle servira de base pour l’analyse des CANETs.

### 0.3 Modèles de bruit dans les CANs

Dans ce chapitre nous étudions les bruits dans les CANs en termes de densité
de probabilité et de densité spectrale de puissance. Nous intéressons de façon
sommaire au bruit thermique et au bruit de scintillement, puis de façon détaillée
au bruit thermique et au bruit créé par la gigue. Le bruit thermique est gaussien
et sa densité spectrale de puissance se blanchit au fur et à mesure que le temps
d’acquisition devient grand devant la constante de temps de l’E/B. La gigue
est la variation aléatoire des instants d’échantillonnage et elle constitue une des
erreurs les plus importantes dans les CAN. Elle comprend la gigue à l’ouverture
et la gigue d’horloge. La gigue d’horloge est causée par le bruit de phase de
l’horloge qui peut être un oscillateur libre ou une boucle à verrouillage de phase.
Le bruit créé par la gigue d’horloge dans le cas d’un oscillateur libre suit un
processus de Wiener et a une densité spectrale de puissance en forme d’une
Lorentzienne. La gigue à l’ouverture est causée par la distribution du signal
d’horloge (buffers). Il s’agit d’un processus banc gaussien et sa densité spectrale
de puissance est quasiment blanche.

### 0.4 Modèles d’erreurs dans les CANETs

Dans ce chapitre nous étudions en détail les CANETs. Le signal à la sortie du
système est donné par les relations (4) et (5). On peut noter une partie idéale qui
consiste en des repliements aux multiples de la fréquence d’échantillonnage du
signal ce qui est normal car l’échantillonnage se traduit dans le domaine spectral
par la périodisation du spectre du signal. Cependant on note aussi l’apparition
d’une composante perturbatrice aux diviseurs de la fréquence d’échantillonnage.
Cette composante provient des mismatchs entre les différentes voies.


```
YDC ( f )
fs
```
##### =

##### +∑∞

```
k =−∞
```
```
Regular part
︷ ︸︸ ︷
[
1 +
```
##### 1

##### M

##### M ∑− 1

```
m =
```
```
δOm (. )
```
##### ]

```
O 0 δ ( f − kfs )
```
##### +

##### ∑+∞

```
k ̸=0[ M ]
−∞
```
##### 1

##### M

##### [ M − 1

##### ∑

```
m =
```
```
ζ − mkδmO
```
##### ]

```
O 0 δ ( f − k
```
```
fs
M
```
##### )

##### ︸ ︷︷ ︸

```
Spurious part
```
##### (4)

```
YAC ( f )
fs
```
##### =

##### +∑∞

```
k ̸=0[ M ]
−∞
```
##### 1

##### M

##### [ M − 1

##### ∑

```
m =
```
```
ζ − mkδHm (. )
```
##### ]

##### H 0 (. ) X (. )

##### ︸ ︷︷ ︸

```
Spurious part
```
##### ∣

##### ∣

##### ∣

##### ∣

```
f − kfMs
```
##### +

##### +∑∞

```
k =−∞
```
```
Regular part
︷ ︸︸ ︷
[
1 +
```
##### 1

##### M

##### M ∑− 1

```
m =
```
```
δHm (. )
```
##### ]

##### H 0 (. ) X (. )

##### ∣

##### ∣

##### ∣

##### ∣

```
f − kfs
```
##### (5)

Nous pouvons également exprimer le mismatch de fonction de transfert comme
combinaison du mismatch de gain, time-skew et bande à travers la relation (6).
Cette relation montre que le mismatch de gain agit sur la partie réelle de la
fonction de transfert, le mismatch de time-skew agit sur la partie imaginaire de
la fonction de transfert, donc ces deux mismatch sont orthogonaux l’un l’autre.
Par contre le mismatch de fonction de transfert agit à la fois sur la partie réelle et
sur la partie imaginaire. Par conséquent le mismatch de bande peut se combiner
de façon constructive ou destructive avec les mismatch de gain et de time-skew.
C’est pourquoi dans cette thèse nous traiterons ces trois mismatch simultané-
ment.

```
δHm ( f ) = δgmQ 0 ( f ) + δtmQ 1 ( f ) + δfcmQ 2 ( f ) (6)
```
```
where
```
##### 

##### 

##### 

##### 

##### 

```
Q 0 ( f ) = 1
Q 1 ( f ) = j 2 πf Ts
Q 2 ( f ) =
jffc
1+ jffc
```
##### (7)

Les mismatchs étant aléatoires, le SFDR sera aussi une variable aléatoire
qu’on peut caractériser. C’est ainsi que nous pouvons calculer d’une part la
densité de probabilité du SFDR pour une profondeur d’entrelacement paire et
impaire qui est donnée respectivement par les formules (9) et (8). Les figures
(7), (8) et (9) montrent la distribution statistique du SFDR pour des mismatchs
de gain, time-skew et bande. On peut voir que la distribution statistique suit
bien la densité de probabilité analytique calculée.
D’autre part nous pouvons calculer de combien il faut réduire l’amplitude des
mismatch pour obtenir le SFDR désiré avec un niveau de confiance spécifique.
La forumule (10) nous dit qu’avec un niveau de mismatch ayant un ecart type de


sigma _σa_ , on peut obtenir un _SF DR_ ( _η_ )avec un niveau de confiance de _η_. Ceci
permet au concepteur analogique de mesurer l’effort de calibration à fournir
pour atteindre les performances désirées.

(^030405060708090100)
500
1000
1500
2000
2500
SFDR in [dB]
Number of occurences
By simulation
By formula
Figure 7: PDF of a two-channel TI-ADCs with a gain mismatch of 1 % and with
a input sinusoid of amplitude 1 V
(^0405060708090)
500
1000
1500
2000
2500
3000
3500
4000
4500
5000
SFDR in dB
Number of occurences
By simulation
By formula
Figure 8: PDF of a two-channel TI-ADCs with a time-skew mismatch of 1 %, a
sampling frequency of 320 MHz and with a input sinusoid of amplitude 1 V and
a frequency of 137 MHz


(^030405060708090)
500
1000
1500
2000
2500
3000
3500
4000
4500
5000
SFDR in dB
Number of occurences
By simulation
By formula
Figure 9: PDF of a two-channel TI-ADCs with a bandwidth mismatch of 1 %,
a sampling frequency of 320 MHz and with a input sinusoid of amplitude 1 V, a
frequency of 137 MHz and a cutoff frequency of 160 MHz
_p_ ( _SF DR_ ) =

##### 1

##### F ′

##### [

##### F −^1 ( SF DR )

```
] fmax
```
##### (

##### F −^1 ( SF DR )

##### )

```
= α
```
##### M − 1

##### 2

```
se − s (1− e − s )
```
```
M − 3
2
```
##### ∣

##### ∣

##### ∣

```
s = σ 2 M
aCa
10 − SF DR 10
```
##### (8)

_p_ ( _SF DR_ ) = _αs_ (1− _e_ − _s_ )

```
M − 4
2
```
##### [ M − 2

##### 2

```
e − serf (
s
2
```
##### )+

##### 1

##### √

```
2 πs
```
```
e − s (1− e −
s 2
)
```
##### ]∣

##### ∣

##### ∣

```
s = σ 2 M
aCa
10 − SF DR 10
(9)
```
```
SF DRdB ( η ) =−10 log 10
```
```
Caσ^2 a
M
−10 log 10 K ( η, M ) (10)
```
### 0.5 Calibration des CANETs

La calibration des CANETs que nous proposons se décompose en deux par-
ties indépedantes: l’estimation et la correction. L’estimation utilise un filtrage
passe-bas combiné avec un filtre à retard fractionnaire pour estimer simultané-
ment les mismatchs de gain, time-skew et bande à travers l’expression du mis-
match de fonction de transfert en fonction du mismatch de gain, time-skew et
bande comme illustré sur la Fig 10. Cette estimation est aveugle c’est-à-dire
que le signal d’entrée est inconnu. On suppose juste qu’il est stationnaire et à
bande limitée. La Fig. 11 montre le temps de convergence pour les mismatchs
de gain, time-skew et bande. On peut voir qu’avec 10-K échantillons on peut
avoir les estimées des trois mismatchs.


##### -

```
δm ˆ g δm ˆ τ δm ˆ fc
```
```
Q 1 ( z ) Q 2 ( z )
```
##### 

##### 

##### 6

##### - + 

##### 6

##### 

##### 

##### +

##### 6

##### 

##### 

##### +

#####  7 7

```
zm ( k )
```
```
z 0 ( k )
```
```
∆ zm
− −
```
```
e ( θθθm, k )
```
```
∆ˆ zm
```
```
HLP ( z )
```
- _HLP_ ( _z_ )

```
ym ( k )
```
```
y 0 ( k )
```
```
Q 0 ( z )
```
##### -

- _Hmdl_ ( _z_ )

##### -

```
δh ˆ m
```
```
Figure 10: Adaptive filtering structure
```
La compensation utilise une représentation vectorielle des signaux de sor-
tie pour identifier la matrice responsable de la distorsion, puis cette matrice là
est inversée pour corriger les erreurs. La Fig. 12 montre la structure de com-
pensation avec deux voies. On peut noter que par simulation nous avons des
corrections de l’ordre de 35 dB comme le montre la Fig. 12 où est represent
le SFDR avant at après calibration pour une fréquence d’échantillonnage de
340 MHz avec des mismatchs de gain de 1%, time-skew de -1% et bande de 2%.
Cependant au fur et à mesure qu’on se rapproche de la fréquence de Nyquist
les performances s’évanouissent. Ceci est du au fait que la bande du signal
s’agrandit, ce qui diminue la portion de bande sur laquelle porte l’estimation
d’une part et d’autre part la correction devient de moins en moins précise car le
mismatch de fonction de transfert n’est plus négligeable devant un (le mismatch
de fonction de transfer est un filtre passe haut).

Des mesures ont été faites sur une carte FPGA Zynq SoC sur laquelle est
connecté un émetteur/récepteur contenant deux CAN que nous avons entrelacés.
Le banc de mesure est illustré la Fig. 13. La Fig. 15 montre le spectre du signal


```
Number of K-samples
```
```
0 5 10 15 20
```
```
Estimated mismatches in %
```
```
-1.5
```
```
-1
```
```
-0.5
```
```
0
```
```
0.5
```
```
1
```
```
1.5
```
```
2
```
```
Convergence of Estimation
```
```
estimated gain mismatch
exact gain mismatch
estimated skew mismatch
exact skew
estimated bandwidth mismatch
exact bandwidth
```
```
Figure 11: Simulation of the Convergence of mismatch estimation
```
de sortie avant et après calibration. On peut voir que le spur du aux mismatchs
a été réduit de 38 dB. La Fig. 14 montre le niveau de correction en fonction
de la taille des filtres utilisés. On constate que la correction augmente au fur
et mesure que l’ordre des filtres augmente. Mais à partir d’un ordre de 51 la
correction ne s’améliore plus et ceci correspond à une compensation de 38 dB.
Ce chapitre se termine par une synthèse sur un circuit numérique. La puissance
consommée est d’environ 10 mW et la surface de 0_._ 035 mm^2.


(^30020406080100120140160)
35
40
45
50
55
60
65
70
75
80
Frequency in MHz
SFDR in dB
Before calibration
After Calibration
Figure 12: SFDR before and after correction with a two-channel TI-ADCs with
1% gain mismatch, -1% time-skew mismatch and 2% bandwidth mismatch. The
sampling frequency is 340 MHz.
Figure 13: Test bench used for the measurements


```
20 30 40 50 60 70 80
```
```
10
```
```
15
```
```
20
```
```
25
```
```
30
```
```
35
```
```
40
```
```
Number of taps
```
```
Improvement in dB
```
Figure 14: Reduction of spurious magnitude with the number of taps of correc-
tion filters

```
Frequency in MHz
```
```
Magnitude in dB 0 10 20 30 40 50 60 70
-200
```
```
-150
```
```
-100
```
```
-50
```
```
0
Before Calibration
```
```
Frequency in MHz
Magnitude in dB^010203040506070
```
```
-200
```
```
-150
```
```
-100
```
```
-50
```
```
0
(a) After Calibration
```
(b)
Figure 15: Measurement results of the output spectrum before and after cali-
bration


### 0.6 Conclusion

Dans ce travail, nous avons proposé une modèle déterministe et statistique pour
analyser la nonlinéarité dans les E/B bootstrappés pour les signaux single-ended
et pour les signaux différentielles. Ceci nous a permis de montrer que dans les
structures bootstrap l’harmonique 2 est dominante et peut être réduite par un
montage différentiel. Dans les structures différentielles, la densité de probabilité
de la distorsion de second ordre a été calculée et nous avons également relié le
niveau de distorsion en fonction du mismatch et du niveau de confiance. Ce
chapitre se conclut avec le modèle mathématique du CAN qui sera utilisé pour
l’entrelacement.

Ensuite dans le second chapitre, nous avons modélisé les bruits dans les CAN
en termes de densité de probabilité et densité spectrale de puissance. Une at-
tention particulière a été portée sur le bruit thermique et la gigue.

Puis dans le troisième chapitre, nous avons modélisé les erreurs dans les
structures entrelacées. Le signal de sortie a été représenté comme une com-
posante idéale et une composante perturbatrice crée par les mismatchs entre les
différentes voies. Une analyse statistique nous a également permis d’exprimer
le SFDR désiré en fonction du niveau de mismatch et du niveau de confiance.

Le dernier chapitre présente la méthode de calibration que nous proposons
pour calibrer le convertisseur. Elle se base sur une estimation aveugle des mis-
matchs à travers un filtrage passe-bas et une filtre à délai fractionnaire. La
compensation utilise une représentation matricielle du CANET pour corriger
les erreurs. Les résultats montrent qu’on peut obtenir des corrections entre 30
et 40 dB et que l’estimation converge avec moins de 10-K échantillons.

Comme perspectives, on peut envisager la prise en compte de la nonlinéarité
de l’E/B dans l’entrelacement et utiliser la méthode établie dans ce travail pour
analyser d’autres erreurs comme l’injection de charge et l’excursion d’horloge.


## Chapter 1

# Introduction

### 1.1 Background and Motivation

The continuing demand for ever-higher wireless data rate system has resulted in
higher bandwidth standards such as LTE-Advanced or IEEE 802.11.ac requir-
ing for instance bandwidth up to 160 MHz. This increases the requirements on
Analogue-to-Digital Converters (ADCs) because in radio receivers, the signal
should be sampled at a rate equal at least to the bandwidth.

Fig. 1.1 shows a conventional radio receiver (superheterodyne). The com-
plexity of this architecture grows linearly with the number of standards and
channels. This is a strong limitation because mobile devices should integrate
multiple bands and cohabitation of old standards such as GSM with new ones
such as LTE-Advanced is desirable in order to enable users to connect worldwide.
This has resulted in the definition of Software Defined Radio (SDR) concept.
The idea behind SDR is that the same hardware architecture can be reconfig-
ured to handle any radio standard. It is achieved by replacing conventional
analog signal processing such as channel selection or filtering in conventional
radio receiver by digital signal processing. This is done by pushing the ADC
close to the antenna as shown on Fig. 1.2.

### 1.2 High Speed ADCs Design Challenges

Replacing analog parts such as mixers with digital ones requires faster and more
accurate converters. However, requirements on high speed is often contradictory
with high accuracy and low power consumption. To illustrate it, Fig. 1.3 shows
a recent survey across popular stand alone ADC architectures (Pipeline, Flash,
Sigma-Delta and Successive Approximation Register) from 1999 to 2014 [1]. It
can be noticed that when the resolution increases, the speed decreases.


```
Antenna
```
Preselection Filter

##### LNA IRF

```
Channel selection
Filter
```
##### ADC

##### ADC

##### I

##### Q

##### DSP

##### LO

```
Shared One receiver per channel
```
##### IF

```
LO Baseband
```
```
Figure 1.1: Conventional superheterodyne architecture.
```
```
Filter
```
##### LNA

```
Wideband
```
##### ADC

##### DSP

```
Shared One DSP per channel
```
```
Figure 1.2: The ideal software defined radio architecture.
```

```
Effective Number Of Bit (ENOB)
```
```
Sampling frequency in MHz
```
```
Figure 1.3: Stand alone ADCs performance survey from 1999 to 2014.
```
### 1.3 Time-Interleaved ADCs

A possible way to achieve a high product speed-resolution with a reasonable
power consumption is by designing Time-Interleaved ADCs (TI-ADCs) [2]. The
first step consists in building high resolution sub-ADCs at relatively low speed.
For mobile handset applications, the power-efficiency is a critical issue. There-
fore Pipeline and Successive Approximation Register (SAR) architectures emerge
as candidates for this purpose since they can achieve simultaneously high reso-
lution with a low power. Then the second step is to interleave these sub-ADCs,
so that they work alternatively as if they were effectively a single high resolution
ADC but working at a much higher rate. This is shown on Fig. 1.4.

### 1.4 Related work on TI-ADCs

Time-Interleaved (TI) architectures have emerged as a good way to provide
high speed data converters with relatively slow circuits. Unfortunately in this
kind of architecture, new errors emerge and give rise ton nonlinear distortion
which significantly degrade the resolution of the overall TI-ADC. These errors
come from discrepancies between the individual sub-ADCs in the system and are
commonly referred to as channel mismatch errors. They consist of gain, time-
skew, bandwidth and offset mismatch errors and they should be mitigated [2] [3].

There are two possible ways to deal with channel mismatches. The first is
to complexify the analog circuit design of the ADC in order to reduce the mag-
nitude of the original mismatches at the cost of more power consumption and
area. But this increases the time-to-market of the ADC. The second solution
is to alleviate the design and to correct the errors with a calibration technique.
Depending of the nature of the input signal, calibration techniques can be clas-
sified into two different categories.


##### ADC 0

##### ADCM − 1

##### MUX

##### S/H 0

##### S/HM − 1

```
x ( t ) y[n]
```
```
Figure 1.4: Time Interleaved ADCs architecture.
```
Foreground calibration techniques estimate the channel mismatches by in-
terrupting the normal TI-ADCs operation and applying a known signal like a
sinewave at its input [4]. Then the output of the TI-ADCs is compared to the
expected output that would have been obtained with no mismatches. In this
way, the effect of each mismatch can be measured and corrected. The drawback
of foreground calibration techniques is that the ADC has to be taken offline
every time that the calibration is carried out. In addition the mismatches may
change due to temperature variations and aging. As a consequence for applica-
tions such as mobile communication systems, foreground calibration techniques
are not suitable because the ADC has to be always on. However they can easily
be used in applications such as instrumentation where the device can be cali-
brated off before being used.

In background calibration techniques, the ADC operation continues when
the calibration is being performed. The mismatches are continuously estimated
and corrected. These techniques can be subdivided into semiblind and blind.
Semiblind background calibration techniques combine the input signal with a
test signal that will be used for the calibration [5]. In blind background cal-
ibration techniques, no test signal is used [6]. Blind background calibration
techniques are the most difficult to design because they should track and adjust
to the changing operation conditions of ADCs in demanding environments with
rapidly changing temperatures. In addition, they should work with no informa-
tions or with little a priori informations on the input signal such as statistics.

When the calibration uses a feedback to the analog front-end of the ADC, it is
a mixed signal calibration [7][8]. When it is done entirely in the digital domain,
the calibration is said to be fully digital [9][10][5]. Mixed signal calibration
techniques are popular in current TI-ADCs chips but fully digital calibrations
are more and more desired because they require no custom redesign of the analog


front-end of the ADC [8].
Several works have been done on correcting the gain, time-skew and off-
set mismatches in TI-ADCs [11] [12] [10] [7] [13] [6] [14] [15] [16] , but little
work has been done on bandwidth mismatches. In [5] [17] [18], some bandwidth
mismatch calibrations are proposed for two channels ADCs but they dont take
into account the time-skew and gain mismatch. Indeed bandwidth mismatch
is frequency dependent and is likely to combine constructively or destructively
with time-skew and gain mismatch as we will demonstrate in this thesis. There-
fore these three mismatches should be treated jointly for more optimality. In
[19], a calibration method for gain, time-skew and bandwidth mismatches us-
ing a feedforward equalizer is proposed, but the algorithm takes a long time
to converge. In [20], a calibration of frequency response mismatch is proposed
by modeling transfer function as polynomial with variable order differentiators
and coefficients. This was done for only two channels and the decomposition
in differentiator filters is more accurate for time-skew mismatch correction than
for bandwidth mismatch. In [21], a fully digital frequency response mismatch
compensation algorithm for TI-ADCs is proposed using correlations between
TIADC samples at two different frequency shifted images for mismatch esti-
mation. In addition most of these calibration techniques were only tested with
behavioral simulations, they have not been synthesized on chips in order to
measure power and area consumption.

### 1.5 Goal, Contribution and Thesis Organization

As pointed out in section 1.4, most of the calibration methods of the state of
art are either suboptimal since they don’t handle all the mismatches together,
limited to a number of channels, have a low convergence speed, or have not been
implemented on chips to evaluate the consumed resources. The main objective
of this work is to propose a new calibration technique that overcomes these
limitations. We propose a fully digital blind background calibration of gain,
time-skew, bandwidth and offset mismatches in TI-ADCs. The contributions of
this work are:

- An original time and frequency domain representation which defines the
    transfer function mismatch and models it as a combination of the gain,
    time-skew and bandwidth mismatch and formulates the problem of cali-
    bration.
- The demonstration of a relationship between the gain, time-skew and
    bandwidth mismatch errors which highlights the necessity of a joint cali-
    bration of these three mismatches for more optimality.
- An adaptive and simultaneously blind estimation of the gain, time-skew
    and bandwidth mismatches. The mismatches can be estimated with an
    accuracy of respectively 98%, 94% and 88% for gain, time-skew and band-
    width mismatches. The algorithm converges with less than 10K-samples
    which is faster compared to the state of art to our knowledge.
- A joint compensation of the gain, time-skew, bandwidth and offset mis-
    match errors simultaneously. Our technique was tested on a two-channels


```
ADCs board from Analog Devices and measurement results show that the
linearity can improved by almost 40 dB.
```
- A calibration scheme that can be applied to any interleaved factor with a
    high flexibility, thus reducing the time-to-market of TI-ADCs.
- A statistical characterization of noise in ADCs in terms of Probability
    Density Function (PDF) and Power Spectral Density (PSD).
- A deterministic and a statistical model in time and in frequency domain
    of bootstrapped S/H both for single ended and differential architectures.
    For differential bootstrapped S/H the mismatches between the p-channel
    and the n-channel should be less than 1% to obtain substantial second
    harmonic distorsion in the order of 100 dB.

This thesis is organized as follow. Chapter 2 gives an analysis of non-
idealities of a single ADC and the analog variables responsible for this non-
idealities are precisely identified. Then a mathematical model of the output of
a single ADC in function of its gain, time-skew, bandwidth and offset is pro-
posed. Chapter 3 complements this model of a single ADC with a statistical
description of noises in ADCs in terms of Probability Density Function (PDF)
and Power Spectral Density (PSD). These noises include quantization, thermal,
jitter and flicker noises. Chapter 4 proposes a general framework describing
simultaneously all mismatches together in TI-ADCs. Statistical laws are ana-
lytically derived. They convert SFDR and THD into matching requirement and
therefore provide key rules for TI-ADCs designers. In chapter 5, we present the
digital calibration we propose for channel mismatches correction. Numerical
simulations and measurements are carried out to verify the correctness of the
algorithm. Performances are also presented for ASIC synthesis in term of power
and area consumption. Conclusion and perspectives of this work are in chapter 6

```
The following publications were done during the course of this work:
```
[7] **G. Kamdem De Teyou** , Hervé Petit and Patrick Loumeau. "Cali-
bration of all mismatches in Time-Interleaved ADCs", _IEEE Transactions on
Circuits and Systems - II_ , submitted 2015.

[6] **G. Kamdem De Teyou** , Hervé Petit and Patrick Loumeau. "Adaptive
and Joint Blind Calibration of Gain, Time-skew and Bandwidth Mismatch Er-
rors in Time-Interleaved ADCs", _IEEE Electronic Letters_ , accepted 2015.

[5] **G. Kamdem De Teyou** , Hervé Petit and Patrick Loumeau. "Adap-
tive and Digital Blind Calibration of Transfer Function Mismatch in a Time-
Interleaved ADCs", _IEEE New Conference on Circuit and Systems_ , 2015.

[4] **G. Kamdem De Teyou** et al. "Statistical Analysis of Noise in Broad-
band and High Resolution ADCs", _IEEE International Conference on Electronic
Circuit and Systems_ , 2014.

[3] **G. Kamdem De Teyou** et al. "Statistical Analysis of Harmonic Dis-
torsion in Bootstrapped Sample and Hold Circuit", _IEEE PRIME Conference_ ,


##### 2014.

[2] **G. Kamdem De Teyou** et al. "Mismatch Requirement Analysis in
Bootstrapped S/H", _GdR System on Chip- System In Package Symposium_ , 2014.

[1] S. Paquelet, **G. Kamdem De Teyou** and Y. Le Guillou "TI-ADCs
SFDR Requirements Analysis", _IEEE New Conference on Circuit and Systems_ ,
2013.



## Chapter 2

# Analysis of Analogue to

# Digital Converters

## Introduction

Analogue-to-Digital Converters (ADCs) are the fundamental interface between
the physical world where signals are analog and digital processing circuits widely
used because of their noise immunity, reconfigurability and flexibility. They
sample continuous-time analogue signal and convert it into a discrete digital
representation. The conversion process consists always into two steps: sampling
which is discretization in time and quantization which is discretization in ampli-
tude. ADCs have become a key element in almost all applications of electronics
such as radar, radio receiver, instrumentation, audio etc...

This chapter gives an analysis of the internal behavior of a single ADC. First,
common ADC performances specifications are given. Then S/H architectures
are explored with their non-idealities. The principal limitations include time-
skew, bandwidth limitation and the signal dependency of the on-resistance. A
precise analysis of this last limitation is provided. The bootstrap technique
is well known to reduce this signal dependency of this on-resistance but some
nonlinearities remain due to parasitic capacitances, mobility degradation and
back gate effect. This results in a second order harmonic spurious which can be
reduced with a differential architecture. However mismatch between channels
limits this technique. In this chapter, we provide a deterministic model in time
and in frequency domain of bootstrapped S/H both for single ended and differ-
ential architectures. A statistical analysis of bootstrapped S/H for differential
signal in function of mismatches is proposed and also the probability for the
Harmonic Distortion (HD) to be lower than a critical value for any mismatch
dispersion. Therefore, for a level of performance determined by a minimum HD
and its probability of achievement we can specify the required mismatch dis-
persion. This practical information becomes of relevant importance to establish
robust design with safe margins.
In section 2.4, the most popular quantization architectures are analysed
regarding the speed, the accuracy, the area and the power consumption. The
last section of this chapter proposes a mathematical model of the output of an


```
Digital output
```
```
Discrete-time analog input
```
```
Offset referred to the input (analog domain)
```
```
Offset referred to the output (digital domain)
```
```
Figure 2.1: Static characteristic of an ADC with offset
```
ADC in function of its gain, time-skew, bandwidth and offset.

### 2.1 ADC Performance Specifications

ADC performance specifications quantify the errors that are caused by the ADC
itself. ADC performance specifications are generally categorized in two ways:
DC accuracy and dynamic performance.

#### 2.1.1 DC Accuracy

The DC specifications for the converter tell how the device performs for steady-
state analog inputs.

**Offset error**

Ideally, the output code for 0V is 0. But in practice for a real ADC, this is
not the case. Offset error as illustrated on Fig. 2.1 is the constant shift in
tension introduced by the ADC across its characteristic. Offset can be positive
or negative and it is a common problem with ADC. Offset error can be easily
compensated by calibration.

**Gain error**

The gain error of an ADC indicates how well the slope of an actual transfer
function matches the slope of the ideal transfer function. Fig. 2.2 shows the
static characteristic of an ADC with gain error.

**Integral and Differential Non-Linearities error**

Nonlinearities errors are local variations of code transition levels which can not
be expressed linearly. They are defined after correcting for linear (offset and
gain) errors. It consists of Integral Non-Linearity (INL) and Differential Non-
Linearity (DNL).


```
Digital output
```
```
Discrete-time analog input
```
```
Ideal ADC with a gain G
```
```
Actual ADC with a gain error∆ G
```
##### G G + ∆ G

```
Figure 2.2: Static characteristic of an ADC with gain error
```
The INL is the distance between the actual decision level and the decision
level of an ideal ADC that has been gain and offset corrected expressed in LSB
units. The INL measures the deviation of the characteristic from a straight line.

```
IN Lm =
```
```
Vm − Vom
q
```
##### (2.1)

Where _Vom_ = ( _m_ −^12 ) _q_ is ideal transition level of code _m_ and _Vm_ =
( _m_ −^12 ) _q_ + _qIN Lm_ is the real transition level of code _m_.

The DNL expresses the difference between the actual and the ideal code bin
widths in LSB units. If DNL exceeds 1 LSB then there is the possibility to have
a missing code at the output.

```
DN Lm =
```
```
Vm +1− Vm
q
−1 = IN Lm +1− IN Lm (2.2)
```
```
Figure 2.3 shows the characteristic of an ADC with non-linearities.
```
#### 2.1.2 Dynamic Performances

Dynamic performances tell how much noise and distortion have been introduced
into the sampled signal and the accuracy of the converter for a given input
frequency and sampling rate.

**Spurious Free Dynamic Range**

The Spurious Free Dynamic Range (SFDR) is the ratio of the rms of the funda-
mental signal to the rms of the strongest spurious regardless of where it comes
from in the spectrum.

```
SF DR = 20 log 10
```
##### (

##### S

```
Smax
```
##### )

##### (2.3)


```
Digital output
```
```
Discrete-time analog input
```
```
Linear
```
```
Nonlinear
```
```
qINL 3
```
```
Figure 2.3: Static characteristic of an ADC with nonlinearities
```
Where _S_ is the rms of the fundamental signal and _Smax_ the rms of the highest
spur which may or may not be an harmonic of the fundamental signal.

**Total Harmonic Distortion**

The Total Harmonic Distortion (THD) is the ratio of the rms of the fundamental
signal to the root-sum-square of its harmonics :

```
T HD = 20 log 10
```
##### (

##### S

##### D

##### )

##### (2.4)

Where _D_ is the root-sum-square of all harmonic components.

**Signal to Noise Ratio**

The Signal to Noise Ratio (SNR) is defined as the ratio of the power of the full
scale fundamental signal by the total power of noise:

```
SN R = 20 log 10
```
##### (

##### S

##### N 0

##### )

##### (2.5)

Where _N_ 0 is the rms of noise. For an ideal ADC with a sine input, the noise
consists only of quantization noise and the SNR is given by [22]:

_SN R_ = 6_._ 02 _N_ + 1_._ 76 (2.6)
Where _N_ is the resolution of the ADC. In practice the measured SNR is
inferior to this theoretical value and we should take into account the others
sources of noise excluding harmonic distorsion.

**Signal to Noise and Distorsion Ratio**

Signal to Noise and Distorsion Ratio (SNDR) is defined as the ratio of the rms
of the signal amplitude to the rms of all other spectral components including
harmonics, but not DC [23]. SNDR is a good indicator for the overall perfor-
mance of the ADC because it includes all components which make noise and
distorsion.


```
SN DR = 20 log 10
```
##### (

##### S

##### N 0 + D

##### )

##### (2.7)

Where D is the rms of harmonic distortions , _N_ 0 is the total noise excluding DC
component and harmonic distortions and S the rms of the fundamental signal.
SNDR, THD and SNR are linked by the relation:

```
SN DR =−10 log 10
```
##### (

##### 10 − T HD/^10 + 10− SNR/^10

##### )

##### (2.8)

**Effective Number of Bit**

If we solve (2.6) in _N_ considering noise and all distorsion components , we obtain
the Effective Number Of Bits (ENOB) defined as :

##### EN OB =

##### SN DR − 1. 76

##### 6. 02

##### (2.9)

**Figure of Merit**

A popular indicator used to compare ADC is the Figure Of Merit (FOM). It is
given by :

```
F OM =
```
##### P

```
2 ENOBfs
```
```
( pJ/step ) (2.10)
```
Where _fs_ is the sampling rate and P the power consumption. This parameter
is commonly used in published report as it is based on measured quantities and
calculates something that has a meaningful value (energy per conversion step).

### 2.2 Analysis of a Basic CMOS Sample and Hold

In ADCs, quantization is not instantaneous. The signal should be maintained
to a constant value to process quantization. This is the function of the Sample
and Hold (S/H) circuit which samples the voltage of the continuous-time signal
and holds its value at a constant level for a minimum period.

The simplest S/H consists of two buffer amplifiers, a transistor-switch and
a storage capacitor as illustrated in figure 2.4. During the sampling mode,
the transistor-switch is _ON_ and the input signal charges or discharges the hold
capacitor so that the voltage _y_ ( _t_ )across the capacitor is practically proportional
to the input voltage _x_ ( _t_ ). This stage goes from _nTs_ − _βTs_ to _nTs_ , with _βTs_ the
acquisition time which is taken as a fraction of the sampling period. The circuit
is governed by a first order linear Ordinary Differential Equation (ODE) with
constant coefficients:

```
y ( t ) + RonC
```
```
dy ( t )
dt
```
```
= x ( t ) and nTs − βTs ≤ t ≤ nTs (2.11)
```
With _Ron_ the on-resistance of the transistor-switch. During the hold mode, the
switch is _OF F_ and the input signal is disconnected from the capacitor. The
voltage across the capacitor is stored as the sampled value _y_ [ _n_ ]. The hold mode
goes from _nTs_ to( _n_ + 1) _Ts_ − _βTs_ :


##### C

##### -

##### ?

```
Clock
```
```
input buffer Output buffer
```
```
x ( t )
```
##### R

##### C

```
y [ n ]
y [ n ]
```
#####  -

```
(a) (b)
```
Figure 2.4: Open-loop S/H diagram (a) and its equivalent first order model (b).

```
y ( t ) = y [ n ] = y ( nTs ) and nTs ≤ t ≤( n + 1) Ts − βTs (2.12)
```
```
There are several non-idealities in this circuit.
```
#### 2.2.1 Time-skew

Time-skew _t_ 0 is a short and constant delay between the moment when sampling
has to be done and the moment when it is really done. Indeed on die, clock
signal must be driven to S/H. For this purpose, buffers are inserted along clock
path to regenerate and amplify clock signal in order to ensure satisfactory edge
at arrival as shown on Fig. 2.5. A typical buffer consists in two inverters in
cascade.

Time-skew comes from propagation delay of clock signal and transition time
in inverters. Time-skew is in the order of some few nanosecond (ns). On a single
ADC, time-skew produces no error but only acts as a fixed delay on sampling
process. But in a Time-Interleaved ADCs (TI-ADCs), it can produce significant
errors as we will see in chapter 4.

#### 2.2.2 Bandwidth limitation

S/H of Fig. 2.4 can be reduced to an RC low-pass filter which has a time
constant _τ_ = _RonC_. To ensure accurate sampling, the sampling duration _βTs_
should be several time bigger than the time constant. A common metric is the
number of time constants _Non_ as defined in [24]:

```
Non =
```
```
βTs
RonC
```
##### (2.13)


```
c
C
```
```
c
C
```
```
c
C
```
```
Clock S/H
```
##### - 

```
t 0
```
#####  -

```
t 0 : Propagation delay + Transition delay in buffers
```
```
Source clock
```
```
Clock at S/H
```
```
Figure 2.5: Clock distribution circuit of a single ADC.
```
Precision S/H is typically designed with _Non_ ≥ 7 [24]. The maximum allowable
sampling frequency in this context is obtained from (2.13) as:

```
fs =
```
```
β
NonRonC
```
##### (2.14)

#### 2.2.3 Signal dependency of the on-resistance

In the sampling mode of the S/H of Fig. 2.4, the on-resistance of the transistor
switch is approximately given by [25]:

```
Ron =
```
##### 1

```
μCoxWL ( Vgs − Vth − Vds 2 )
```
##### (2.15)

Where _W_ , _L_ , _Cox_ , _Vgs_ , _Vth_ and _Vgs_ are respectively the width and length of
the MOS transistor, the gate capacitance per unit area, the gate-to-source volt-
age, transistor threshold voltage and the drain-to-source voltage. _Vds_ 2 is most
of the time negligible with respect to _Vgs_ − _Vth_. The source _S_ of the transistor
is connected to the input signal _x_ ( _t_ ). Therefore the gate-to-source voltage _vgs_
becomes dependent of the input signal. As a result, the whole resistance _Ron_ is
signal dependent and this will cause significant distortion in the sampled voltage
on the hold capacitor.

**The bootstrap circuit**

Some techniques have been proposed on the analog side to mitigate this dis-
tortion. For example the use of a PMOS switch in parallel with an NMOS
switch [26]. But the most popular is the clock bootstrapping [27] [28] [29] [30]
which removes a significant portion of nonlinearities by making the value of
the transistor-switch gate-source voltage as independent as possible of the in-
put signal. The logical structure of the bootstrapped circuit is shown in Fig. 2.6.


##### C

##### -

```
r r
```
```
r
r
```
```
r
r
```
```
r r r r
```
```
vdd
```
##### Φ Φ

##### Φ

##### Φ

##### Φ

##### M 1

##### N 1

##### C 3

```
c
x ( t )
```
```
y[n]
c
```
```
Figure 2.6: Logical structure of the bootstrap circuit.
```
When the sampling switch _M_ 1 is _OF F_ ,Φ = 0and _C_ 3 is precharged to _vdd_.
WhenΦ = 1, a constant voltage equal to _vdd_ is established between the gate and
the source of _M_ 1. Ideally, _Ron_ is now independent of the input signal. But in
practice, parasitic capacitance at node _N_ 1 , mobility degradation and back gate
effect limit the linearity that can be achieved. At a first order we can consider
that _Ron_ still depends of the input signal, but with a weakly linear dependency:

```
Ron ( x ) = bon + aonx (2.16)
```
With _aon_ and _bon_ two constants which depend on the circuit. Simulation results
confirm this assumption as we can see on Fig. 2.7 which shows the on-resistance
of a bootstrapped circuit in function of the input signal in 65 nm CMOS tech-
nology. We see that the on-resistance varies quasi linearly with the input signal.

Therefore, without loss of generality we consider that the time constant _τ_
varies linearly with the input signal as written in (2.17). _b_ is the static compo-
nent of the time constant and _a_ is the dynamic component of the time constant.
Montecarlo simulation of a bootstrapped circuit in 65 nm CMOS process shows
that _b_ and _a_ can be modeled as random variables normally distributed as we
can see on Fig. 2.8 and Fig. 2.9.

Simulation results show that _a_ and _b_ are highly correlated as shown on Fig.
2.10 where _a_ is plotted in function of _b_. A correlation coefficient _ρ_ ( _a, b_ ) = 0_._ 9
was obtained between _a_ and _b_. As a consequence, we can consider that _a_ can be
expressed linearly in function of _b_ as in (2.17). In others words, this means that
_a_ can be determined knowing _b_. In Appendix. A, this correlation is explained
through some analytical calculation.


```
0 0.2 0.4 0.6 0.8 1 1.2
105
```
```
110
```
```
115
```
```
120
```
```
125
```
```
130
```
```
135
```
```
Input signal in V
```
##### R

```
on
```
```
in
```
##### Ω

Figure 2.7: Simulations result of the on-resistance of a bootstrapped S/H as
a function of the input signal in 65 nm CMOS process with supply voltage of
_vdd_ = 1_._ 2 V.

(^0810121416182022242628303234)
20
40
60
80
100
120
Slope _a_ in ns V−^1
Number of occurrences
Figure 2.8: Statistical distribution of the slope a in 65 nm CMOS process with
supply voltage of _vdd_ = 1_._ 2 V.


(^0859095100105110115120125130135)
20
40
60
80
100
120
140
160
180
_b_ in ns
Number of occurrences
Figure 2.9: Statistical distribution of the constant resistance _bon_ in 65 nm CMOS
process with supply voltage of _vdd_ = 1_._ 2 V.
_τ_ ( _x_ ) = _RonC_ = _b_ + _ax
a_ = _α_ + _βb_

##### (2.17)

For the simulation of Fig. 2.10, we obtained _α_ =− 39_._ 5 ns V−^1 and _β_ =
0_._ 5 V−^1.

**Single ended architecture**

We can solve the ODE of (2.11) by considering the linear dependency of the
time constant _τ_ ( _x_ )with the input signal _x_ of (2.17). For this purpose we make
the following assumptions:

- The sampling duration _βTs_ is several times bigger than the time constant
    _τ_ in order to ensure accurate sampling.
- The S/H is weakly nonlinear i.e _ax_ ≪ _b_ in (2.17)
- There is no memory effect, i.e the charge of the hold capacitor is set to
    zero after each sample

The _nth_ sample at the S/H output can be written as a desired component
and an undesired component (see Appendix A.2):

```
y [ n ] =
```
```
desired
︷ ︸︸ ︷
( h ⋆ x )( nTs )−
```
```
a
b
```
##### {

```
( h ⋆ x^2 )( nTs )−
```
##### (

```
h ⋆
```
##### [

```
x. ( h ⋆ x )
```
##### ])

```
( nTs )
```
##### }

##### ︸ ︷︷ ︸

```
undesired component
```
##### (2.18)


```
90 95 100 105 110 115 120 125 130
5
```
```
10
```
```
15
```
```
20
```
```
25
```
```
30
```
```
35
```
```
b in ns
```
```
a
```
```
in ns V
```
```
−
1
```
Figure 2.10: Correlation between _a_ and _b_ in 65 nm CMOS process with supply
voltage of _vdd_ = 1_._ 2 V.

With _h_ the impulse response of the linear S/H which is obtained by taking
the static component _b_ of the time constant _τ_ ( _x_ ):

```
h ( t ) =
```
##### 1

```
b
```
```
exp(−
t
b
```
```
) u ( t ) (2.19)
```
_u_ ( _t_ )in (2.19) is the Heaviside step function. The desired part is what should be
obtained if the on-resistance were totally constant while the undesired compo-
nent comes from the variations of the on-resistance with the input signal _x_ ( _t_ ).
As _a_ → 0 , the resistance becomes constant and the undesired component de-
creases. (2.18) is far more simple than what has been obtained in [31].

Taking the particular case of a sinusoidal input _x_ ( _t_ ) = _A_ sin(2 _πf_ 0 _t_ ), the
Discrete Time Fourier Transform (DTFT) _Y_ ( _f_ )of _y_ [ _n_ ]is:

```
Y ( f )≃
```
```
Offset
︷ ︸︸ ︷
aA^2
4 b
```
##### [

```
H ( f 0 ) + H (− f 0 )− 2
```
##### ]

##### +

```
desired part
︷ ︸︸ ︷
1
2
```
```
AH ( f 0 ) δ ( f − f 0 )
```
##### +

```
aA^2
4 b
```
```
H (2 f 0 ) K ( f 0 ) δ ( f − 2 f 0 )
︸ ︷︷ ︸
second harmonic
```
##### (2.20)

_H_ ( _f_ )in (2.20) is the transfer function of the S/H and _K_ ( _f_ ) = _H_ ( _f_ )− 1.

We notice that firstly the S/H exhibits an offset which can easily be removed
digitally. Secondly the nonlinearity is mostly characterized by the presence of
a dominant harmonic of second order which will degrade the dynamic perfor-
mances such as SFDR and SNDR.


```
Frequency According to (2.20) By simulation
```
```
HD 2 in dB 61.25 61.20
```
Table 2.1: Simulation results of a S/H with _τ_ ( _x_ ) = (1_._ 25 _e_ −10 + 2_._ 33 _e_ − 11 _x_.
The input signal is _x_ ( _t_ ) = 0_._ 6 sin(2 _πfot_ ), _fo_ = 20MHz, _fs_ = 300MHz.

Fig. 2.11 presents the simulation of the output spectrum of a S/H with a
time constant varying linearly with the input signal and Tab. 2.1 compares
the simulation results with (2.20). Considering a sinusoidal input, the worst
spurious is effectively at 2 _f_ 0. The Second Harmonic Distortion ( _HD_ 2 ), defined
as the ratio of the power of fundamental signal to the power of the second
harmonic matches very well with (2.20).

```
−150 0 20 40 60 80 100 120 140 160
```
```
−100
```
```
−50
```
```
0
```
```
Frequency MHz
```
```
f 0 2 fo 3 fo
```
```
fs
2
```
```
Fundamental
```
```
Harmonic 2
```
```
Offset
```
```
Power in dB/bin
```
Figure 2.11: Output spectrum of a S/H with _τ_ ( _x_ ) = (1_._ 25 _e_ −10 + 2_._ 3 _e_ − 11 _x_.
The input signal is _x_ ( _t_ ) = 0_._ 6 sin(2 _πfot_ ), _fo_ = 20MHz, _fs_ = 300MHz and the
number of fft points is 16384
.

**Differential architecture**

As the worst spurious created by nonlinearity in a bootstrapped S/H is the
second harmonic, it can be mitigate with a differential architecture. To do it,
for an input signal _x_ ( _t_ ), we send the signal _x_ 1 ( _t_ ) =^12 _x_ ( _t_ )on the first channel
and on the second channel we send the signal _x_ 2 ( _t_ ) =−^12 _x_ ( _t_ ). Fig. 2.12 shows
a differential bootstrap S/H circuit.


```
Bootstrap
```
```
r
```
##### C

##### C

```
Bootstrap
```
```
r
```
```
x 1 ( t )
```
```
x 2 ( t )
```
-

##### -

```
y 2 [ n ]
```
```
y 1 [ n ]
```
```
Figure 2.12: Differential Bootstrap S/H circuit.
```
From (2.20), the second harmonic of the _ith_ 1 _,_ 2 channel is obtained by dividing
the amplitude by two :

```
H 2 i =
```
```
aiA^2
16 bi
```
```
Hi (2 f 0 ) Ki ( f 0 ) (2.21)
```
Where _Hi_ ( _f_ ) =1+ _j_ 21 _πfbi_ is the transfer function of the _ith_ channel and _Ki_ ( _f_ ) =
_Hi_ ( _f_ )− 1. The time constant of channel _i_ 1 _,_ 2 is _τi_ = _bi_ + _aixi_ ( _t_ ). The second
harmonic of the whole S/H is obtained by making the difference of the second
harmonic of channels 1 and 2:

##### H 2 = H 21 − H 22

##### ≃

```
λA^2
16
H (2 f 0 ) K ( f 0 )
```
```
[ θ
λ
+ K (2 f 0 ) + H ( f 0 )
```
```
]∆ b
b
```
##### (2.22)

_b_ is the average value of _b_ , _H_ =1+ _j_^12 _πfb_ , the average transfer function, _K_ =

_H_ − 1 , _λ_ = _αb_ + _β_ and _θ_ = _αb_. _α_ and _β_ are defined in (2.17)

```
The HD 2 can be derived from (2.22) and (2.20) as :
```
```
HD 2 = 10 log 10
```
##### [

```
| c |^2 /
```
```
(∆ b
```
```
b
```
##### ) 2 ]

##### (2.23)

With _c_ the complex number given by:

```
c =
```
```
8 H ( f 0 )
λAH (2 f 0 ) K ( f 0 )
```
##### [

```
θ
λ + K (2 f^0 ) + H ( f^0 )
```
##### ] (2.24)


```
Frequency ∆ bb = 0. 062 ∆ bb =− 0. 041
```
```
Simulated HD 2 77.09 80.23
```
```
HD 2 with (2.23) 76.96 80.52
```
Table 2.2: Simulation results of a differential bootstrapped S/H with _β_ =
0_._ 125 ns. The input signal is _x_ ( _t_ ) = 0_._ 6 sin(2 _πfot_ ), _fo_ = 20MHz and _fs_ =
300 MHz.

Table. 2.2 compares some simulation results with (2.23). As we can see this
analytical model match very well and the _HD_ 2 is considerably better than what
was obtained in section 2.2.3.

**Probabilistic Description of the Second Harmonic Distortion**

Device mismatches are inherent to any manufacturing processes whatever the
technology is (CMOS, SiGe, ...) and are commonly described by random vari-
ables normally distributed. Since these mismatches are responsible for channel
mismatch errors, it is convenient to rely on a probabilistic characterization of
the time constant mismatches. As a consequence, the harmonic distortion is
modeled by a statistical distribution related to the standard deviation _σ_ of time
constant mismatch as in [3].
Readily,∆ _bb_ = _σε_. With _ε_ ∼N(0 _,_ 1). From (2.23) the _HD_ 2 can be rewritten
as:

```
HD 2 = 10 log 10
```
```
(| c | 2
σ^2 ε^2
```
##### )

```
= F ( ε^2 ) (2.25)
```
As the _HD_ 2 is function of the random variable _ε_^2 , it is also a random variable
whose dispersion depends on standard deviation of mismatches _σ_. The random
variable _ε_^2 follows a chi-squared distribution with one degree of freedom _χ_^12 and
the function _F_ is strictly monotone. Therefore the Probability Density Function
(PDF) _p_ of the _HD_ 2 can be obtained from that of _ε_^2 with a change of variables.
All calculations done, we find that the PDF of the _HD_ 2 is:

```
p ( HD 2 ) =
```
##### 1

##### F ′

##### [

##### F −^1 ( HD 2 )

```
] χ^12
```
##### (

##### F −^1 ( HD 2 )

##### )

##### =

##### √

##### C

```
2 π
```
```
log(10)
10 σ
```
##### 10 −

```
HD 2
```
(^20) exp
−

##### [

```
C
2 σ^210
```
```
− HD 102
```
##### ] (2.26)

Fig. 2.13 shows the statistical distribution of the _HD_ 2 obtained by simula-
tion and the calculated PDF. Both curves match almost.

**Reliability of** _HD_ 2

Using an analogy to the usual yield, we introduce the robustness criterion
_HD_ 2 ( _η_ ), that states the _HD_ 2 remains higher than this threshold value with


(^080869298104110116122128134)
2
4
6
8
10
12
14
16
18
Simulation
Formula
_HD_ 2 in dB
N x Probability
Figure 2.13: Statistical distribution of second harmonic distortion of a dif-
ferential bootstrapped S/H in 65 nm CMOS process with an input signal
_x_ ( _t_ ) = 0_._ 6 sin(2 _πfot_ ), _fo_ = 20MHz, _fs_ = 300MHz, a relative mismatch of
1.2 % and N = 50 points.
a probability 1 − _η_.
_η_ = _p_

##### (

```
HD < HD ( η )
```
##### )

```
= 1− p
```
##### (

```
ε^2 < F −^1 ( HD ( η )
```
##### )

```
= 1−erf
```
##### (

##### √√

##### √

##### √

##### [

```
F −^1 ( HD ( η ))
```
##### ] 2

##### 2

##### )

##### (2.27)

```
erfis the Gauss error function.
Inverting (2.27) with respect to SF DR ( η )gives :
```
```
HD 2 ( η ) =−10 log 10
σ^2
| c |^2
```
```
−10 log 10 K ( η ) (2.28)
```
With _K_ ( _η_ )≃ _π_ 2 (1− _η_ )^2. (2.28) states the _HD_ 2 remains higher than the threshold
value _HD_ 2 ( _η_ )with the probability 1 − _η_ allowing to control the reliability of
any mismatch calibration process like in [3].
Fig. 2.14 shows the harmonic distortion law as a function of the standard
deviation of mismatches for a frequency of 20 MHz. To obtain a _HD_ 2 of 100 dB
with a reliability of 0.999, the mismatch should be less or equal than 1 %.

#### 2.2.4 Charge Injection and Clock Feedthrough

Others non-idealities of S/H circuits are charge injection and clock feedthrough.
Fig. 2.15 represents the equivalent model of the transistor in the triode re-
gion. _Cgs_ and _Cgd_ are respectively the gate-source and the gate-drain parasitic
capacitance.
When the transistor turns OFF, the channel charge _Qch_ is dispersed into
the source and drain. The channel charge depends on the gate-source voltage
[32]:


```
10 −1 100
90
```
```
95
```
```
100
```
```
105
```
```
110
```
```
115
```
```
120
```
```
125
```
```
130
η = 0.001
η = 0.2
η = 0.4
η = 0.5
```
```
Standard deviation σ of mismatch in %
```
##### HD

```
2
```
```
in dB
```
```
Figure 2.14: Harmonic distortion law
```
```
Qch =− W LCox ( Vgs − Vth ) (2.29)
```
Only the fraction injected in the drain will produce an error which will depend
linearly on the input signal. If we denote _kch_ this fraction, then the charge
injection error is given by :

```
∆ ych =
```
```
kchQch
C
```
##### =−

```
kchW LCox ( Vgs − Vth )
C
```
##### (2.30)

The charge injection appears as a gain error and an offset. Similarly, the
clock feedthrough offset error∆ _yclk_ due to the gate-drain parasitic capacitance
_Cgd_ is given by [32] :

```
∆ yclk =−
Cgd
Cgd + C
```
```
Vdd (2.31)
```
Table. 2.3 gives some order of magnitude of the ON resistance, charge in-
jection gain and clock feedthrough offset error in 28 nm HPL process.

### 2.3 Others Sample and Hold architectures

#### 2.3.1 Close loop S/H

The signal-dependent charge injection mentioned above can be avoided by op-
erating the switch at a constant potential, which can be realized by enclosing
the switch in a feedback loop to create a virtual ground. Fig.2.16 shows a basic
closed-loop S/H circuit following this idea [33].
The drawback of this architecture is that it uses two opamps in tracking
mode with a positive feedback loop. Therefore a heavy compensation is needed
in order to avoid instability. This naturally reduces the speed of the circuit.
Further more, for an interleaving factor of _M_ , 2 _M_ opamps will be needed. This
will consume a large portion of the total power as well as a large chip area.


##### R

##### C

```
Cgs Cgd
```
##### R

```
x ( t )r r y [ n ]
```
##### ?

```
Figure 2.15: Charge injection and clock feedthrough.
```
```
Parameter Symbol or formula Value Unit
NMOS transistor width W 1.4 μm
NMOS transistor length L 30 nm
Overlap length xd 4 nm
Oxide thickness tox 1.4 nm
Oxyde Permittivity εox 3. 51 × 10 −^13 F cm−^1
Gate capacitance per
unit area
```
```
Cox = εox/tox 25 fFμm−^2
```
```
Threshold voltage Vth 0.536 V
Supply voltage Vdd 1 V
Gate-drain parasitic
capacitance
```
```
Cgd = εoxW ( L + 2 xd ) / 2 tox 0.4 fF
```
```
Electron mobility μ 400 cm^2 V−^1 s
Hold capacitor C 4 pF
Charge injection
coefficient
```
```
kch 0.5
```
```
Charge injection gain Gch = kchW LCox/C 1. 3 × 10 −^4
Clock feedthrough offset yclk =
Cgd
Cgd + CVdd 0.2 V
On resistance Ron ≃
```
##### [

```
μCoxWL ( Vdd − Vth )
```
##### ]− 1

##### 46 Ω

Table 2.3: Parameter values used to model S/H non-idealities in 28 nm HPL
technology


```
Figure 2.16: Typical close loop S/H circuit
```
#### 2.3.2 Switched Capacitor S/H

A commonly used S/H is Switched Capacitor (SC) S/H shown on Fig. 2.17.
The sampling is performed passively i.e without the opamp making the signal
acquisition fast. The clocks _CLK_ 1 and _CLK_ 2 have a frequency _fs_ and are
in phase opposition. When _CLK_ 1 is high, _CLK_ 2 is low, and the input signal
charges the capacitor. It is the sampling mode. During the Hold mode, _CLK_ 1 is
low, _CLK_ 2 is high and the sample loaded accross _C_ is transfered to the output.
To avoid charge injection, _CLK_ 1 _p_ is slightly advanced to _CLK_ 1. This is known
as bottom plate sampling technique [34] [33].

#### 2.3.3 Double Sampling S/H

The double-sampling is a technique to double the sampling rate of Switched
Capacitor (SC) S/H circuit with only a minor increase in power consumption
[35] [36]. Fig. 2.18 shows a double sampling SC S/H. The clocks _CLK_ 1 and
_CLK_ 2 have a frequency _fs_ and are in phase opposition. When _CLK_ 1 is high,
_CLK_ 2 is low, and the first sample is loaded accross _C_ 1. Then when _CLK_ 1 is
low, _CLK_ 2 is high, the first sample loaded accross _C_ 1 is forwarded to the ADC
for quantization and the second sample is loaded accross _C_ 2 and so on. As a
result, every _Ts/_ 2 there is a sample at the output of the ADC and the sampling
frequency is thus doubled. To avoid charge injection, bottom plate sampling
technique is used.

### 2.4 Quantization

After the sampling process, the amplitude of the different samples can theoreti-
cally take any value in a continue range of values. Quantization is the conversion
of a discrete-time analogue signal into a digital signal. All the values at the out-
put of the quantizer are multiple of an elementary quantity _q_ called quantization
step or Least Significant Bit (LSB). The LSB and the resolution _N_ are related
by (2.32) :

```
q =
Vmax − Vmin
2 N − 1
```
##### (2.32)


_CLK_ 1

```
CLK 1 p
```
```
CLK 2
```
_CLK_ 2 ADC

```
Figure 2.17: Switch Capacitor S/H circuit
```
```
x ( t )
```
```
CLK 1
```
```
CLK 1 p
```
```
CLK 2
```
```
CLK 2
```
```
C 1
```
```
CLK 2 p
```
```
CLK 2 CLK 1
```
```
CLK 1
```
```
C 2
```
ADC

```
Figure 2.18: Double sampling technique
```

```
V 1 V 2 V 3 V 4 V 5 V 6 V 7
```
```
q = 000
```
```
001
```
```
010
```
```
011
```
```
100
```
```
101
```
```
110
```
```
111
```
```
Digital output
```
```
Discrete-time analog input
```
```
Figure 2.19: Quantization characteristic
```
Where _Vmin_ and _Vmax_ respectively are the upper and lower extremes of the
voltages that can be coded.

Quantization structures can be implemented in many different ways. Dif-
ferent architectures are suitable for some specific applications regarding the
speed, the accuracy, the area and the power consumption. The most popu-
lar quantization architecture are: Flash, Pipeline, Sigma-Delta and Successive
Approximation Register (SAR).

#### 2.4.1 Flash Architecture

Flash converters [18] [13] [37] [38] [39], are the simplest and fastest converters
in the ADC family. The parallel nature of Flash converter makes it suitable
for high speed high bandwidth applications. The drawback of this architecture
is that it is power hungry, consumes significant die area and offers only low
to moderate output resolution. This limit Flash converters to high frequency
applications such as data satellite communication, radar processing, sampling
oscilloscopes and high-density disk drive.

In a Flash converter, a resistance ladder is used to generate voltage reference
levels. Then a constant voltage _Vref_ is applied to the whole resistance ladder,
and the voltage levels between the resistances are used as reference levels. The
analog input signal or the output of the S/H is then compared to the refer-
ence levels from the resistance ladder to determine which level is closest. This
means that to get a precision of _N_ bits in the ADC, 2 _N_ resistances and 2 _N_ − 1
comparators are required.
Since all reference levels are compared to the analog signal simultaneously,
the conversion time is constant, independent of the number of bits. This also
means that a Flash ADC is very fast. However, the drawback is that the hard-
ware grows exponentially with the number of bits. The power consumption also
grows exponentially.


ADC type Resolution Sampling
rate

```
Characteristic
```
Flash 4 to 8 bits 100 MHz to
5 GHz

- High speed
- High bandwidth
- High power consumption
- Large area
- Matching difficulties

Pipeline 12 to 16 bits 10 MHz to
100 MHz

- High throughput
- Moderate bandwidth
- Low power consumption
- Moderate area
- Self calibration technique

SAR 10 to 16 bits 50 kHz to
5 MHz

- Very high resolution and accu-
    racy
- Low bandwidth
- Low power consumption

Sigma-Delta 14 to 20 bits 100 kHz to
500 MHz

- High output resolution
- Moderate to high speed
- High bandwidth
- Moderate power consumption
- On Chip digital filtering

```
Table 2.4: Comparisons of differents converters achitectures
```

##### + − + − + −

##### R

##### R

##### R

##### R

```
Resistance Encoder
ladder
```
```
Comparator
array
```
```
Analog input
```
##### LSB

##### MSB

```
Vref
```
```
Figure 2.20: A 2 bits Flash converter.
```
#### 2.4.2 Successive Approximations Architecture

Successive Approximation Register (SAR) architectures are very popular for
high resolution and low to medium speed applications. Current architectures
have capabilities of sampling at several megahertz with a resolution ranging
from 9 to 18 bits[37].

The basic architecture of the SAR ADC consists of a DAC, an analog com-
parator and a SAR logic [40][41]. Fig. 2.21 shows a 4 bit SAR using a bi-
nary weighted capacitor DAC array. The DAC capacitor array has four binary-
weighted ( _Ci_ = 2 _iC_ 0 , for i=0 to 3) and one redundant ( _Cr_ = _C_ 0 ) capacitors.
In the figure, the switches are shown in the sampling mode where the ana-
log input is constantly charging or discharging the parallel combination of all
capacitors.
The hold mode is initiated by opening _Sg_ and by connecting _Sr, S_ 0 _...S_ 3 to
ground. The voltage at node X becomes− _Vin_.
After that, _S_ 3 is connected to _Vref_ and this forces _Vx_ to be:

```
Vx =− Vin +
```
##### C 3

```
Ctotal
```
```
Vref =− Vin +
```
##### 1

##### 2

```
Vref (2.33)
```
Where _Ctotal_ = 2 _NC_ 0 denotes the total capacitance of the DAC capacitor array.
If _Vx_ is negative then _Vin_ is greater than _Vref/_ 2 and we have _D_ 3 = 1. Otherwise
we have _D_ 3 = 0and the top plate of _C_ 3 will be reconnected to ground. For an


N bits SAR ADC, this process iterates N times, with a smaller capacitor being
switched each time, until the conversion is finished. In the _ith_ iteration, _Vx_ can
be expressed by:

```
Vx ( i ) =− Vin +
```
```
CIN ( i )
Ctotal
```
```
Vref (2.34)
```
Where _CIN_ ( _i_ )is the total capacitance connected to _Vref_ at the _ith_. At the end of
conversion, _Vx_ approaches zero. The transition level of code _m_ = ( _DN_ − 1 _...D_ 0 )
is:

```
Vm =
```
##### ∑ N − 1

```
i =0 DiCi
Ctotal
```
```
.Vref (2.35)
```
```
Due to process variations, capacitors are not exactly matched and we have:
```
```
Ci = 2 iCo (1 + εi ) (2.36)
```
Where _εi_ is the mismatch of capacitor _Ci_. Finally (2.35) can be written as:

```
Vm =
```
##### ∑ N − 1

```
i =0 Di^2
```
```
iC 0
2 NC 0
```
```
.Vref +
```
##### ∑ N − 1

```
i =0 Di^2
```
```
iεiC 0
2 NC 0
```
```
.Vref
```
```
= Videal ( m ) + q
```
##### N ∑− 1

```
i =0
```
```
Di 2 iεi
︸ ︷︷ ︸
INLm
```
##### (2.37)

In (2.37) we recognize the expression of the INL of the ADC which depends
directly of the N capacitor mismatches of the DAC. This shows that the DAC
is a critical component because the linearity of the ADC is limited by the DAC.
Further more the SAR ADC speed is also limited by the settling time of the
DAC. This makes the accuracy of the SAR converter imposed by the accuracy
of the DAC [42].
(2.37) shows that mismatch _εN_ − 1 on the MSB capacitor is the most signifi-
cant, then follows _εN_ − 2 and so on. These capacitor mismatches can be estimated
directly by measuring the DNL of the ADC:

```
DN L (0) = ε 0
DN L (2^1 −1) = 2 ε 1 − ε 0
... = ...
DN L (2 N −^1 −1) = 2 N −^1 εN − 1 − ... − ε 0
```
##### (2.38)

#### 2.4.3 Pipelined Architecture

Pipeline converters are very popular architectures with conversion speeds from
few tens of megahertz to few hundred of megahertz. They have resolution capa-
bilities from 6 to 16 bits. Owing to their high resolution capability and moderate
to high sampling rate, they are more widely used in Charge Coupling Device


```
C 3 C 2 C 1 C 0 Cr
```
```
SAR Control Logic
```
##### +

##### −

##### D 3 ...D 0

```
Sin
```
```
Sg
```
```
Vref
```
```
Vin
S 3 S 2 S 1 S 0 Sr
```
```
DAC capacitor array
```
##### X

```
Figure 2.21: Successive Approximation Register.
```
(CCD), imaging, digital receiver, communication base stations, cable modem
and Ethernet device. However for high speed applications beyond the GHz
range, Flash topology is still the architecture of choice. A typical pipeline con-
verter is shown on Fig. 2.22 [18] [37].

The converter divides the conversion task into several consecutive stages.
Each of them consists of a sample and hold circuit, an m-bit sub-ADC (usually
a Flash ADC), and an m-bit DAC. The sample and hold, DAC, subtraction
block and amplification form an arithmetic unit called the multiplying digital-to-
analog converter (MDAC). First, the sample and hold of the first stage requires
the input signal. Then the n-bit Flash converter converts the sampled signal to
digital data. The conversion result forms the most significant bits of the digital
output. This same digital output is sent to an m-bit digital to analog converter,
and its output is subtracted from the original sampled signal. The residual
analog signal is then amplified and sent to the next stage in the pipeline to be
sampled and converted as it was in the first stage. This process is repeated
through as many stages are necessary to achieve the desired resolution.

#### 2.4.4 Delta-Sigma Architecture

The block diagram of a basic Delta Sigma (∆Σ) converter is shown on Fig. 2.23.
The elementary DS converter is a one bit sampling system. An analog signal
applied to the input of the converter needs to be relatively slow so the converter


##### ADC

##### S/H +

##### +

##### −

```
Analog input Stage 1 Stage 2 Stage N
```
```
Digital Correction
```
```
Digital
```
```
output
```
##### DAC

```
x2
```
```
Figure 2.22: Pipeline Converter Architecture.
```
can sample it multiple times, a technique known as oversampling. The sam-
pling rate can be hundreds of times faster than the digital results at the output
ports. Each individual sample is accumulated over time and averaged with the
other input-signal samples through the digital/decimation filter to produce a
high-resolution slower digital code [37] [18] [43].

#### 2.4.5 Summary on quantization architecture

The performances of SAR, Pipeline, Flash and SD are summarized in Table.
2.4. More details can be found in [37] [38] [43] [18] [44].

From Table. 2.4, Pipeline and SAR architectures emerge as candidates for
low power high resolution ADCs. In the past decades, Pipeline ADCs have dom-
inated over SAR ADCs because analog design was easier and capacitors were
occupying too much die and area and were lower quality than today. However
today as CMOS technology evolves, analog design becomes a very challenging
task forcing the designers to use as much digital solution as possible. Further
more capacitors become better in term of matching and density. As a result
SAR ADCs is attracting more and more designers and are suitable to achieve
high resolution with a high power efficiency due to their dominantly digital
nature, scalable architecture and to the steady improvement in matching and


##### ∫

##### +

##### −

```
∑ Digital Filter
and
Decimator
```
##### −

##### +

##### DAC

```
1 bit
```
```
Vin
```
```
1 bit ADC
N bits
```
```
fs
```
```
Kfs
```
```
Σ−∆Modulator
```
```
Figure 2.23: Delta Sigma ADC.
```
```
Gain
```
##### G

```
Time-skew
```
```
t 0
```
```
Jittered clock
```
```
σjitter
```
```
Bandwidth
```
```
fc
```
```
Offset
```
##### O

```
Thermal
```
```
vthermal
```
```
Noise
```
```
Quantization
```
- INL, DNL
- Gain, Offset
- Quantization noise

```
Figure 2.24: Mathematical model of a single ADC
```
density of Metal-Finger Capacitors(MFC). But the drawback is that they suffer
from speed limitations.

### 2.5 Summary and mathematical model at the ADC output

Typical S/H analyzed above can be reduced at a first order approximation to as
low-pass filters with a cutoff frequency _fc_ = 2 _πR_^1 _onC_ where _Ron_ is the combined
resistance of all transistors and buffers and _C_ the hold capacitor. _G_ , _t_ 0 and
_O_ are respectively the gain, the time-skew and offset of the ADC. We denote
_h_ ( **p** _, t_ )the impulse response of the equivalent low-pass filter parameterized by
the vector **p** = ( _G, t_ 0 _, fc_ )and _H_ ( **p** _, f_ )its transfer function. Taking into the


account the memory effect of the hold capacitor and the acquisition time _βTs_ ,
it can be found that:

```
H ( p , f ) = Hmem ( f )
```
##### G

```
1 + jffc
```
```
e − j^2 πft^0 (2.39)
```
```
Where Hmem ( f ) =^1 − αe
```
```
− j 2 πβfTs
1 − αe − j^2 πfTs and α = e
```
```
− RβTonsC. The demonstration is
```
detailed in Appendix A.4. For ADCs of concern, the acquisition time _βTs_ is
much more greater than the time constant _RonC_ (at least 7 times). Therefore,
_Hmem_ ( _f_ )≃ 1. Nonetheless, _α_ can be taken into account if case arises.

Figure. 2.24 shows the mathematical model of a single ADC. The _nth_ sam-
ple at the ADC output output can be splitted into an AC component, a DC
component and a noise component :

```
y [ n ] = yAC [ n ] + yDC [ n ] + vnoise [ n ] =
```
##### (

```
h ( p ,. ) ⋆ x
```
##### )

```
( nTs ) + O + vnoise [ n ](2.40)
```
where _⋆_ is the convolution operator.

Without loss of generality, the noise component _vnoise_ can be considered
independently as an additive contribution which will be analyzed later in chapter

3. The Discrete Time Fourier Transform (DTFT) of _y_ [ _n_ ]is given by:

```
Y ( f ) = YAC ( f ) + YDC ( f )
```
```
= fs
```
##### +∑∞

```
k =−∞
```
##### {

```
H ( p ,. ) X (. ) + Oδ (. )
```
##### }∣∣

##### ∣

```
f − kfs
```
##### (2.41)

The filtering component _YAC_ is made up of replicas of the fundamental signal
at multiple of _fs_ and the DC component appears as a line spectrum at multiple
of _fs_. This DTFT of the output of a single ADC will be compared to that of
a TI-ADCs. It will enable us to highlight spurious components resulting from
channel mismatch errors.

### 2.6 Chapter conclusion

In this chapter a performance analysis of ADC was presented in terms of DC
specifications and dynamic performance. DC specifications include gain, offset,
INL and DNL and they tell how accurately the quantization is done. Dynamic
performance tell how much noise and distortion have been introduced into the
signal and are commonly described by THD, SFDR, SNDR and SNR.

Then basic CMOS S/H architectures were studied as well as their non-
idealities. These non-idelities consist of clock feedthrough, charge injection,
bandwidth limitation and nonlinearity of the on resistance. Clock feedthrough
can easily be removed digitally since it appears as an offset. Charge injection
can be canceled with a dummy switch or with the bottom plate sampling tech-
nique. The popular method to remove the nonlinearity of the on resistance is


the clock bootstrap technique. Unfortunately some nonlinearities remains due
to the parasitic capacitances, the backgate effect and the mobility degradation.
A deterministic model describing booststrapped S/H circuits both for single
ended and differential architecture was proposed. For single ended architecture,
the second harmonic is dominant and it can be mitigated with a differential
architecture. However mismatches between channels should significantly be re-
duced to obtain high performances in differential architecture.

After that, the most popular quantization architectures were introduced re-
garding the speed, the accuracy, the area and the power consumption. Pipeline
and SAR have emerged as good candidates for low power TI-ADCs. A model
linking the nonlinearities of the SAR ADC to DAC capacitor mismatches was
also proposed.

Finally, the expression of the signal at ADC output was derived as the com-
bination of deterministic component and a noise component. The deterministic
component is entirely described with the gain, time-skew, bandwidth and offset
of the ADC. The next chapter will provide a statistical description of the noise
component.


## Chapter 3

# Noise modeling in ADCs

### 3.1 Introduction

In previous chapter, we studied S/H and quantization architectures. We saw
that ADCs can be characterized by some non-idealities such as nonlinearities,
gain, time-skew, bandwidth and offset. Another problem is that all individual
ADCs are naturally disturbed by noises which constitute a severe barrier to
the achievement of high resolution. Noises include thermal, flicker, jitter and
quantization noise. The goal of chapter document is double. On the one hand,
it aims to study probability density function and power spectral density of these
noises. On the other hand we aim to propose a general framework describing
design requirements in terms of thermal noise, jitter and power consumption for
low noise ADC.

### 3.2 Signal model

The _nth_ sample at the ADC output can be written as :

```
y [ n ] =
```
##### (

```
h ( p ,. ) ⋆ x
```
##### )

```
( nTs ) + O +
```
_vnoise_ [ _n_ ]
︷ ︸︸ ︷
_vthermal_ [ _n_ ] + _vflicker_ [ _n_ ] + _vjitter_ [ _n_ ] + + _vq_ [ _n_ ]
(3.1)
Where _Ts_ is the sampling period, _vthermal_ , _vflicker_ , _vjitter_ and _vq_ are respectively
the thermal, the flicker, the jitter and quantization noise. _O_ the offset of the
ADC and _h_ ( **p** _,._ )is the impulse response of the ADC parameterized by **p** =
( _G, τs, fc_ ).
The total noise power is given by :

```
v^2 noise = v^2 thermal + v^2 flicker + v^2 jitter + vq^2 (3.2)
```
### 3.3 Quantization Noise

#### 3.3.1 Total power

A first order expression of the total power of quantization noise is [45]:


```
vq^2 =
```
```
q^2
12
```
##### +

```
q^2
3
```
(^2) ∑ _N_ − 1
_m_ =0
_Pm_ ( _IN L_^2 _m_ +1+ _IN Lm_ +1 _IN Lm_ + _IN L_^2 _m_ ) (3.3)
Where _Pm_ is the probability of occurence of code _m_ and _N_ the number of bits.
If the ADC is linear, then quantization noise is reduced to _q_
2
12 and the SNR for
a sinusoidal input signal is given by:
_SN Rq_ = 6_._ 02 _N_ + 1_._ 76 (3.4)
Quantization noise is systematic and in practice we should also take into account
the other noise sources. However, most of the time, the ADC is designed such
that the major source of noise is quantization.

#### 3.3.2 Probability Density Function

The Probability Density Function (PDF) of the quantization noise of a linear
ADC is [46]:

```
p ( vq ) =
```
##### 

##### 

##### 

##### 1

```
q
```
##### +

##### 1

```
q
```
##### ∑

```
n ̸=0
```
```
Φ x
```
##### (

```
2 πn
q
```
##### )

```
exp
```
##### (

```
− j 2 πnvq
q
```
##### )

```
− q/ 2 < vq< q/ 2
```
```
0 otherwise
```
##### (3.5)

WhereΦ _x_ is the characteristic function of the input signal. The PDF of the
quantization noise depends on the statistical properties of the input signal. If
Φ _x_ verifiesΦ _x_ (^2 _πnq_ ) = 0for all _n_ ̸= 0, then the quantization noise is uniform.

For the particular case of a zero mean gaussian input signal with a standard
deviation _σx_ , the PDF of quantization noise becomes :

```
p ( vq ) =
```
##### 

##### 

##### 

##### 1

```
q
```
##### [

##### 1 + 2

##### ∑

```
n ̸=0
```
```
cos
```
##### (

```
2 πnvq
q
```
##### )

```
exp
```
##### (

##### −

```
2 π^2 n^2 σx^2
q^2
```
##### )]

```
− q/ 2 < vq< q/ 2
```
0 otherwise
(3.6)
As the ratio _σx/q_ becomes large, the PDF of quantization noise becomes
uniform.

#### 3.3.3 Power Spectral Density

There is no general expression for the PDF of the quantization noise. For a
gaussian input signal with a standard deviation _σx_ , quantization noise becomes
white as the ratio _σx/q_ becomes large [46].

### 3.4 Thermal noise

By definition, thermal noise is an electronic noise generated by thermal agitation
of charge carriers inside an electrical conductor at thermal equilibrium, which


##### C

```
x ( t ) y [ n ]
```
##### C

```
Ron
```
```
von^2 = 2 kBT Ron d f
```
```
vthermal
```
##### ∼

(a) (b)
Figure 3.1: (a): Typical S/H circuit. (b): Thermal noise source in a basic S/H.

happens regardless of any applied voltage. In an ideal resistor _R_ , thermal noise
is white, gaussian and its Power Spectral Density (PSD) is 2 _kBT R_ , where _kB_
is Boltzmann’s constant in joules per kelvin and _T_ is the resistor’s absolute
temperature in kelvins [47].
To examine the impact of thermal noise in any circuits, the first step is to
set all input voltages to zero and add noise source associated to each resistance
of the circuit. Then the second step consists in evaluating the circuit output
voltage in these conditions. Fig. 3.1 (b) shows the circuit for analysis of basic
S/H thermal noise of Fig. 3.1 (a). _Ron_ is the on-resistance of the transistor
switch and _von_ is the white gaussian noise source that model thermal noise of
_Ron_.

#### 3.4.1 Probability Density Function

Thermal noise _vthermal_ at S/H output is gaussian and its total power is _kBCT_ :

```
vthermal ∼N
```
##### (

##### 0 ,

```
kBT
C
```
##### )

##### (3.7)

See proof in Appendix D.0.1

#### 3.4.2 Power Spectral Density

The Power Spectral Density (PSD) of sampled thermal noise at S/H output is
given by:

```
Sthermal ( f ) =
```
##### 1

```
fs
```
```
kBT
C
```
```
1 −exp
```
##### (

```
− 4 Non
```
##### )

```
1 −2 exp
```
##### (

```
− 2 Non
```
##### )

```
cos(2 πffs ) + exp
```
##### (

```
− 4 Non
```
##### ) (3.8)

Where _Non_ is the number of time-constants defined as the ratio of the sampling
duration to the time constant of the sample and hold. The demonstration is
detailed in Appendix D.0.2. To ensure accurate sampling _Non_ should be large.
For example:

```
Non ≥ 7 −→exp
```
##### (

##### −

```
Ts
RonC
```
##### )

##### ≤ 8. 3 × 10 −^7 ≪ 1. (3.9)


```
Sth ( f ) = kBCTf^1 s
```
```
− f 2 s − B 2 B 2 f 2 s f
```
```
kBT
C
```
```
B
fs
```
```
Figure 3.2: Power spectral density of thermal noise
```
Therefore the power of thermal noise is uniformly distributed in the fre-
quency domain and :

```
Sthermal ( f )≃
```
##### 1

```
fs
```
```
kBT
C
```
##### (3.10)

For a bandlimited signal, thermal noise power integrated in signal bandwidth is
_kBT
C_

_B
fs_ , with _B_ the bandwidth of the signal.
Thermal noise decreases when the hold capacitor increases and so the de-
signer can size the hold capacitor sufficiently large to mitigate as possible the
thermal noise. However increasing the hold capacitor limits the sampling fre-
quency of the S/H. Indeed, for sampling accuracy purposes, the maximum sam-
pling frequency is limited to :

```
fsmax =
```
##### 1

```
2 NonRonC
```
##### (3.11)

Therefore the designer has to face a trade-off between the thermal noise, the
sampling frequency and the number of time constants. Considering for example
a sinusoidal signal _x_ ( _t_ ) = _A_ sin(2 _πfot_ ), the Signal to Noise Ratio ( _SN Rthermal_ )
and the Effective Number Of Bit ( _EN OBth_ ) due to thermal noise inside the
nyquist band are respectively:

```
SN Rthermal = 10 log 10
```
##### (

##### A^2 /

```
kBT
C
```
##### )

```
EN OBth =
```
```
10 log 10
```
##### (

```
A^2 /kBCT
```
##### )

##### − 1. 76

##### 6. 02

##### (3.12)

Fig. 3.3 shows the evolution of the sampling frequency and the ENOB in
function of the hold capacitor. Targetting and _EN OBthermal_ of 14 bit, the hold
capacitor should be 6 pF and the sampling frequency should be less than 1 GHz.

### 3.5 Jitter Noise

Uncertainty of sampling times in S/H cause an error given by :

```
vjitter [ n ] = x ( nTs + ε [ n ])− x ( nTs + ε [0]) (3.13)
```

```
0 2 4 6 8 10 12
```
```
12
```
```
13
```
```
14
```
```
15
```
```
16
```
```
0 2 4 6 8 10 12
```
```
0
```
```
1
```
```
2
```
```
3
```
```
4
```
```
5
```
```
6
```
```
7
```
```
8
```
```
9
```
```
10
```
```
Hold Capacitor [pF]
```
##### EN OB

```
thermal
```
```
in [bit]
```
```
Sampling frequency in [GHz]
```
Figure 3.3: Sampling frequency and ENOB due to thermal noise vs Hold capac-
itor. Simulation done with _Non_ = 7, _Ron_ = 15and _A_ = 0_._ 75 _V pp_

Where _ε_ [ _n_ ]is a random time shift at time _nTs_. The jitter _ξ_ is defined as the
sample instant variations :

```
ξ [ n ] ={ ε [ n ]− ε [0]}∼N(0 , σ^2 [ n ]) (3.14)
```
In general, _σ_ ≪ _Ts_. For example, considering our wideband applications, _fs_ ∼
307_._ 2 MHz→ _Ts_ = 3_._ 25 ns. Typical orders of magnitude of _σ_ is some picosec-
onds. Taking _σ_ = 1 ps gives _σ_ = 3× 10 −^4 _Ts_. So (3.13) can be approximated to
:

```
vjitter [ n ]≃ ξ [ n ]
```
```
∂x ( t )
∂t
```
##### ∣

##### ∣

##### ∣

```
t = nTs
```
##### (3.15)

#### 3.5.1 Signal to Noise Ratio

Taking the particular case of a sinusoidal input _x_ ( _t_ ) = _A_ sin(2 _πfot_ ), the total
power of jitter noise is derived from (3.15) as :

```
vjitter^2 =E
```
##### [

```
2 πfoξ [ n ] A cos(2 πfot )
```
##### ] 2

```
= 2 π^2 fo^2 A^2 σ^2
```
##### (3.16)

And the Signal to Noise Ratio ( _SN Rjitter_ ) and the Effective Number Of Bit
( _EN OBjitter_ ) due to jitter are respectively:

```
SN Rjitter [dB] =−20 log 10 (2 πfoσ )
```
```
EN OBjitter =
−20 log 10 (2 πfoσ )− 1. 76
6. 02
```
##### (3.17)

(3.4) shows that the SNR and ENOB decrease with the jitter and the input
signal frequency as plot on Fig. 3.4. This is a significant limiting factor for high


```
100 101 102
```
```
2
```
```
4
```
```
6
```
```
8
```
```
10
```
```
12
```
```
14
```
```
16
```
```
18
```
```
20
```
```
22
σ = 0.1 ps
σ = 1 ps
σ = 10 ps
σ = 50 ps
σ = 100 ps
```
```
Input frequency [MHz]
```
```
ENOB in [bit]
```
```
Figure 3.4: ENOB due to jitter vs input frequency
```
input frequencies. For instance, in order to achieve 14 bit _EN OBjitter_ when
sampling a 100 MHz signal, the total jitter must be less than 75 fs. Achieving
such a low jitter is very challenging. Indeed low jitter is often contradictory
with low power consumption. For example, the PLL Figure Of Merit (FOM) is
defined by [48] :

```
F OMP LL = 10 log 10
```
```
[( σ
P LL
1 s
```
##### ) 2

##### PP LL

```
1 mW
```
##### ]

##### (3.18)

Where _PP LL_ is the power consumption of PLL. Taking a _F OMP LL_ =
− 240 dB (very close to the state of art) leads to a power consumption of up
to 178 mW which is very enormeous for mobile handset applications.

#### 3.5.2 Composition of jitter

The total amount of jitter is the combination of the clock jitter _ξclk_ and the
aperture jitter _ξapt_ which are independent [49]:

```
ξ [ n ] = ξclk [ n ] + ξapt [ n ]
σ^2 = σ^2 clk + σ^2 apt
```
##### (3.19)

_σclk_ and _σapt_ are respectively the standard deviation of the clock and the
aperture jitter in seconds. The Clock jitter is time uncertainty caused by the
clock generator (PLL, oscillators) while the aperture jitter stands for uncertainty
caused by clock distribution (buffer, S/H circuitry).

#### 3.5.3 Aperture jitter

The clock buffer slew rate (SR) translates the thermal noise into time uncer-
tainty called aperture jitter which increases as clock slew rate decreases as de-
picted on Fig. 3.5 and which is given by:

```
σapt =
```
```
vthermal
SR
```
##### (3.20)


```
Thermal noise
```
```
aperture jitter aperture jitter
```
```
Clock with high slew rate Clock with low slew rate
```
```
σapt
```
```
σapt
```
```
tan−^1 ( SR )
```
```
vthermal
```
```
σapt
```
```
Vhigh
```
```
Vlow
```
```
Figure 3.5: Aperture jitter in S/H circuit
```
The Clock Slew rate _SR_ in V ns−^1 is defined as the slope of the clock signal at
transition instants :

##### SR =

```
Vhigh − Vlow
trising
```
##### (3.21)

_Vhigh_ , _Vlow_ and _trising_ are respectively the high level, the low level and the
rising time of the clock as depicted on Fig.3.5. An ideal clock has an infinite
slew rate while a real clock has a finite slew rate. For SysClk (DigRF), _Vhigh_
= 1_._ 2 V, _Vlow_ = 0_._ 3 V and _trising_ = 2 ns (measured between 30 % and 70 % of
_Vhigh_ ) and this gives _SR_ = 0_._ 24 V ns−^1 [50].
A capacitor of 4 pF and a temperature of 300 K give a thermal noise of
0_._ 032 mV rms. Considering SysClk (DigRF) which has a slew rate of _SR_ =
0_._ 2 V ns−^1 , we obtain _σapt_ = 0_._ 13 ps rms.

**Probability density function of aperture jitter**

The aperture jitter _ξapt_ is commonly modeled by a white gaussian process : i.e
we have the following properties∀ _n, m_ [ ]:

- _ξapt_ [ _n_ ]∼N(0 _, σapt_^2 )
- E

##### [

```
ξapt [ n ] ξapt [ m ]
```
##### ]

```
= σapt^2 δ ( n − m )
```
**Power spectral density of sampling noise due aperture jitter**

In [51], the PSD of the noise created by aperture jitter in sampling process has
been established for a periodic signal. Based on that and using the above sta-


```
0 20 40 60 80 100 120 140 160
```
```
−160
```
```
−140
```
```
−120
```
```
−100
```
```
−80
```
```
−60
```
```
−40
```
```
−20
```
```
0
```
```
Frequency [MHz]
```
```
Analytical formula
```
```
Simulation
NFFT = 16384 points
```
```
2 π^2 A^2 fo^2 σ^2 apt
fs
```
```
Magnitude in [dB]
```
Figure 3.6: Power spectral density of aperture jitter noise in S/H with _fo_ =
80 MHz, _σapt_ = 0_._ 13 ps rms, _fs_ = 307_._ 2 MHz and _A_ = 0_._ 75 V _p_

tistical properties, we establish the PSD of any Wide Sense Stationnary Signal
(WSS) _x_ ( _t_ )as :

_Sjitter_ _ _apt_ ( _f_ ) =

```
F requency dependent component
︷ ︸︸ ︷
Sxx ( f )(1− e −^2 π
```
(^2) _f_ (^2) _σapt_ 2
)^2 +
_W hite component_
︷ ︸︸ ︷
1
_fs_

##### ∫+∞

```
−∞
```
```
Sxx ( f 1 )(1− e −^4 π
```
(^2) _f_ 12 _σapt_ 2
) d _f_ 1
(3.22)
The demonstration is detailed in Appendix E. One can see that the aperture
jitter is almost white because the frequency dependent component is negligible
when compared to the white component in high frequencies. For the particular
case of a sinusoidal input _x_ ( _t_ ) = _A_ sin(2 _πfot_ ), we have :
_Sjitter_ _ _apt_ ( _f_ )≃
_F requency dependent component_
︷ ︸︸ ︷
( _πfoσapt_ )^4 _A_^2

##### [

```
δ ( f + fo ) + δ ( f − fo )
```
##### ]

##### +

```
W hite component
︷ ︸︸ ︷
2( πfoσapt )^2 A^2
fs
```
##### ≃

```
W hite component
︷ ︸︸ ︷
1
fs
```
```
2( πAfoσapt ) A^2
```
##### (3.23)

SysClk (DigRF) buffer slew rate is 0_._ 24 V ns−^1 and with a thermal noise of
_vthermal_ = 0_._ 03 mV it produces an aperture jitter _σapt_ = 0_._ 13 ps rms. Simulation
results of noise resulting from sampling a sinusoidal signal with this clock is
presented on Fig. 3.6. We notice that the PSD is effectively white and the
shape matches very well with (3.23)

#### 3.5.4 Clock jitter

Clock jitter is time uncertainty coming from clock phase noise. The clock signal
_CK_ ( _t_ )controlling the S/H can be written as :


```
CK ( t ) = g
```
##### [

```
ωs
```
##### (

```
t +
φOUT ( t )
ωs
```
##### )]

```
= g [ ωs ( t + ε ( t ))] (3.24)
```
Where _g_ is a 2 _π_ periodic function, _φOUT_ the clock phase noise and _ε_ the random
time shift defined in 3.15.
The rms clock jitter after _n_ clock cycles as defined in (3.15) is [52] :

```
σclk^2 [ n ] =
```
##### 1

```
ω^2 s
```
##### E

##### [∣∣

```
∣ φOUT ( nTs )− φOUT (0)
```
##### ∣

##### ∣

##### ∣

##### 2 ]

##### =

##### 2

```
ω^2 s
```
##### [

```
RφOUT (0)− RφOUT ( nTs )
```
##### ]

##### =

##### 4

```
ω^2 s
```
##### ∫+∞

```
−∞
```
```
SφOUT (∆ f ) sin^2 ( π ∆ f nTs ) d (∆ f )
```
##### (3.25)

∆ _f_ is the offset frequency. _RφOUT_ and _SφOUT_ are respectively the autocorre-
lation function and the PSD of phase noise. The shape of _SφOUT_ (∆ _f_ )depends
on how the clock is made. We will analyze the cases of a free-running oscillator
.

**Jitter noise caused by a free-running oscillator in ADC**

−→Probability Density Function :

From equation (3.25), and considering that free-running oscillator phase
noise profile is accurately modeled by _f_^12 characteristic, we observe that clock
jitter linearly increases with cycles. More generally it can be shown that in a
free-running oscillator, clock jitter is a wiener process with gaussian increments
i.e we have the following properties :

- _εclk_ [1] = _λ_ 1
- _εclk_ [ _n_ ] =

```
∑ n
i =1 λi
```
- _λi_ ∼N(0 _, σ_^2 _clk_ )
- E[ _λiλj_ ] = _σ_^2 _clkδ_ ( _i_ − _j_ )

```
−→Power Spectral Density of jitter noise in S/H:
```
In [51], the PSD of the jitter noise has been established for a periodic signal.
Based on that and using the above statistical properties, we establish the PSD
of any Wide Sense Stationnary Signal (WSS) _x_ ( _t_ )as :

```
Sjitter _ clk ( f )≃
```
```
Lorentzian spectrum
︷∫ ︸︸ ︷
+∞
```
```
−∞
```
```
Sxx ( f 1 )
f 12 σ^2 clkfs
π^2 f 14 σ^4 clkfs^2 + ( f − f 1 )^2
```
```
d f 1 (3.26)
```
```
Assuming a sinusoidal x ( t ) = A sin(2 πfot ), Sxx ( f ) = A
```
```
2
4
```
##### [

```
( δ ( f − fo ) + δ ( f +
```
_fo_ )

##### ]

. Then(3.26) becomes :


```
0 50 100 150
−160
```
```
−140
```
```
−120
```
```
−100
```
```
−80
```
```
−60
```
```
−40
```
```
−20
```
```
0
```
```
Analytical formula
```
```
Simulation
```
```
Frequency [MHz]
```
```
Jitter noise magnitude [dB]
```
```
NFFT = 16384 points
```
Figure 3.7: Power spectral density of noise resulting from sampling a sinusoidal
signal _x_ ( _t_ ) = 0_._ 6 sin(2 _πf_ 0 _t_ )with a clock generated by a free-running oscillator.
_fo_ = 75MHz, _σclk_ = 82 fs, _fs_ = 300MHz

```
Sjitter _ clk ( f ) = Nfo ( f ) + N − fo ( f ) (3.27)
```
_Nfo_ is the lorentzian curve given by :

```
Nfo ( f ) =
```
##### A^2

##### 4

```
fo^2 σclk^2 fs
π^2 fo^4 σclk^4 fs^2 + ( f − fo )^2
```
_N_ − _fo_ is obtained by replacing _fo_ by− _fo_ is _Nfo_.
Fig. 3.7 shows simulation results of noise resulting from sampling a sinusoidal
signal with a clock whose jitter follows a Wiener process. We see that the shape
of simulation matches very well with analytical formulas (3.27) and (3.5.4).

### 3.6 Flicker Noise

Flicker noise is a gaussian noise source appearing from the random trapping
of charge carriers at the oxide-silicon interface of MOSFETs [53]. The Power
Spectral Density (PSD) of flicker noise is given by:

```
Sflicker ( f ) =
```
##### K

```
CoxW L
```
##### ·

##### 1

```
f
```
##### (3.28)

Where _K_ , _Cox_ , _L_ and _W_ are respectively the flicker noise coefficient, the gate
oxide capacitance per unit area, the channel length and width of the transistor.
The importance of flicker noise is analysed by measuring the _corner frequency_


```
log( fcorner )
```
```
Noise floor (thermal noise & shot noise)
```
```
f^1
flicker noise
```
```
log( f )
```
##### S

```
flicker
```
```
[dB
```
##### ]

```
Figure 3.8: Power spectral density of flicker, thermal and shot noise
```
[54] which is the frequency where it becomes far negligible with respect to white
noise (thermal and eventually shot noise) as represented on Fig. 3.8.

As example, ADC of [55] has^1 _f_ noise of 0_._ 64 pW/f and a high frequency
noise floor of 0_._ 062 pW Hz−^1.

### 3.7 Conclusion

In this chapter we have analyzed statistical properties of noises that occur in
single ADC. First we demonstrated how INL/DNL increase quantization noise.
For a linear ADC, the total power of quantization noise is equal to the irre-

ductible power of _q_

2
12 where _q_ is the LSB. For gaussian input signals, quanti-
zation noise becomes white and uniformly distributed in the range[− _q/_ 2 _q/_ 2 ]
as the LSB becomes negligible compared to the standard deviation of the signal.

Secondly we saw that thermal noise is gaussian and has a PSD which becomes
white when the number of time constants in the sampling duration increases.
Thermal noise can be mitigated by sizing the hold capacitor sufficiently large.
But usually there is a tradeoff between thermal noise, sampling frequency and
the number of time constants.

Thirdly we saw that jitter noise is a significant limiting factor in ADC espe-
cially in wideband ADC. It consists of aperture jitter and clock jitter. Aperture
jitter stands for uncertainty caused by clock distribution circuitry. It can be
modeled by a white gaussian process which variance depends of clock slew rate
and thermal noise magnitude. With a capacitor of 4 pF, the slew rate must be
higher than 0_._ 2 V ns−^1 to ensure that aperture jitter is lower than 0_._ 13 ps. Noise
caused by aperture jitter in sampling process has a white PSD.

Clock jitter is time uncertainty caused by the clock generator (PLL, oscil-
lators). For free-running oscillators, there is accumulation of clock jitter with


cycles and in sampling process they cause a noise which PSD is a lorentzian
function.

In a PLL the input reference jitter is dominant within the PLL BW and
the VCO jitter is dominant outside the PLL BW. When High bandwith and
high dynamic range ADC system are considered, ultra low jitter performance is
achievable by using some jitter cleaner techniques but at the cost of high power
consumption.

```
Flicker noise is gaussian and has a PSD which decreases with frequency.
```

## Chapter 4

# Time-Interleaved ADCs

# modeling

### 4.1 Introduction

In the previous chapters, we analyzed non-idealities and noises on stand alone
ADCs. However, in order to increase the sampling rate of ADCs beyond a cer-
tain process technology limit, Time Interleaved (TI) ADCs have been proposed
[2]. In this kind of architecture, several sub-ADCs work in an interleaved man-
ner as if they were effectively a single ADC but working at a much higher rate.
The overall sampling frequency is the frequency of one sub-ADC multiplied by
the interleaved factor. Fig. 4.1 shows a TI-ADCs architecture. TI-ADCs find
applications in electronic systems such as radar, radio receiver and high speed
instrumentation.

Time-Interleaved (TI) architectures have emerged as a good way to provide
high speed and high resolution data converters with relatively slow circuits.
Unfortunately in this kind of architecture, new errors emerge and give rise to
nonlinear distortion which significantly degrade the resolution of the overall TI-
ADCs. These errors come from discrepancies between the individual sub-ADCs
in the system and are commonly referred to as channel mismatch errors. They
consist of gain, time-skew, bandwidth and offset mismatch errors.

TI-ADCs have been widely studied for deterministic mismatches [2] [18] [5].
However considering random character of manufacturing process, resulting mis-
matches and spurious become random variables and their description involves
necessarily a statistical modeling. [56] makes a general analysis of random time-
skew mismatch. In [57], Probability Density Function (PDF) of both Signal-
to-Noise Ratio (SNR) and Spurious-Free-Dynamic Range (SFDR) are explicitly
calculated for random gain, time-skew and offset mismatch. [58] provides for-
mula of the expected Signal-to-Noise and Distortion Ratio (SINAD) for random
gain, time-skew and offset mismatch. The novelty of this chapter consists in:

- generalizing the deterministic mismatch model including the bandwidth
    and showing its coupled effect with the time-skew and bandwidth


```
Gain
```
##### GM − 1

```
Time-skew
```
```
τMs − 1
```
```
σjitter
```
```
Bandwidth
```
```
fcM − 1
```
```
Offset
```
##### OM − 1

```
Thermal
```
```
vthermal
```
```
Noise
```
```
Quantization
```
```
τ 0 s fc
0
```
##### G 0 O 0

##### M

##### U

##### X

```
M Ts
```
##### M T

```
s
```
##### + (

##### M

##### −

##### 1)

```
Ts
```
```
Figure 4.1: M Time-Interleaved ADCs
```
- determining the probability density function of SFDR for all mismatches
    including bandwidth
- determining the probability for the SFDR to be lower than a critical value
    for any mismatch dispersion.

Therefore, for a level of performance determined by a minimum SFDR and its
probability of achievement we can specify the required mismatch dispersion.
This practical information becomes of relevant importance to establish robust
design with safe margins.

### 4.2 Time Interleaved ADCs Architecture

In the interleaved architecture of Fig. 4.1, each sub-ADC samples the signal
at the period _M Ts_ and there is a time shift of _Ts_ between the clock of two
consecutive channels as shown on Fig. 4.2 which represents the clock diagram
of the different sub-ADCs.

#### 4.2.1 Clock

The TI-ADCs source clock has a frequency _fs_ = _T_^1 _s_ and can be generated with
an oscillator. A PLL can also be used in order to have a low jitter but at the
cost of a higher power consumption.


##### 6

##### -

-  _Ts_

```
CLK 0
```
##### CLK 1

##### CLK 2

##### CLK 3

```
Figure 4.2: Clock diagram of the sub-ADCs
```
#### 4.2.2 Phase generator

The function of the phase generator is to derive the sub-ADCs clocks of fre-
quency _fMs_ from the original clock of frequency _fs_ as shown on Fig. 4.3. A
Delay-Locked Loop (DLL) can be used for this purpose [59] but Shift Registers
(SR) are better than DLL because they generate less jitter for a given power
budget [60]. Fig. 4.4 shows phase generator for 4 sub-ADCs using SR.

#### 4.2.3 Buffers

Once each sub-ADC clock has been generated, it has to be distributed efficiently
to each sub S/H. A typical way to drive clock signal from phase generator to
sub-S/H is to insert buffers along clock path as in Fig. 4.5. The function of
buffer stages is to regenerate the clock signal in order to ensure satisfactory edge
rate at S/H. A buffer consists of two inverters as represented on Fig. 1.4.


```
Phase Generator
```
```
c c c
```
##### ???

```
Source clock
```
##### ?

```
CLK 0 CLK 1 CLKM − 1 Sub-ADCs Clocks
```
```
Figure 4.3: Sub-ADCs clock created by a phase generator
```
```
r
```
```
r
```
```
D Q r
```
##### Q

```
r
```
```
r
```
```
D Q r
```
##### Q

```
r
```
```
r
```
```
D Q r
```
##### Q

```
r
```
```
r
```
```
D Q r
```
##### Q

```
r
```
```
r
```
```
D Q r
```
##### Q

```
CLK 3 ( f 4 s )
```
```
CLK 2 ( f 4 s )
```
```
CLK 1 ( f 4 s )
```
```
CLK 0 ( f 4 s )
```
_CLK_ ( _fs_ )

```
Sub-ADCs clocks
```
```
Figure 4.4: Shift Registers Phase generator for 4 sub-ADCs
```

```
c c c -
```
```
c c c -
```
```
c c c - S/H 0
```
##### S/H 1

##### S/HM − 1

##### CLK 0

##### CLK 1

##### CLKM − 1

```
Figure 4.5: Clock distribution with inverters
```
### 4.3 Time Domain Analysis

Let’s use de following notations:

- _m_ ∈{ 0 _,_ 1 _, ...M_ − 1 }denotes a given channel.
- _ζ_ = exp

```
( j 2 π
M
```
##### )

```
, the Mth unitary root.
```
- _Gm_ , _tm_ , _fcm_ , _Om_ , _hm_ and _Hm_ are respectively the gain, time-skew, cut-off
    frequency, offset, impulse response and transfer function of channel _m_.

By extending (2.40) to interleaving, the AC and the DC components of the
TI-ADCs output are:

```
yAC [ n ] = ( hn [ M ] ⋆ x )( nTs ) yDC [ n ] = On [ M ] (4.1)
```
### 4.4 Frequency domain representation

Ideally, all the sub-ADCs should be identical. But in practice there are some
mismatches among them. Let’s use the following notations for the mismatches:

- _gm_ = (1 + _δgm_ ) _g_ 0 , with _δgm_ the relative gain mismatch of channel _m_.
    Similarly we define _δfcm_ , _δhm_ , _δHm_ and _δOm_.
- The relative time-skew mismatch of channel _m_ , _δtm_ is defined respective
    to the sampling period _Ts_ : _δtm_ = ( _tm_ − _t_ 0 ) _/Ts_.

Channel 0 is considered as the reference channel in our analysis. Using (4.1)
and the definition of mismatches, the Discrete-Time Fourier Transform (DTFT)
_YDC_ and _YAC_ of _yDC_ and _yAC_ can be found:


```
Gain Time-skew Bandwidth Offset
```
```
Qa 1 − j 2 πf Ts
jffc
1+ jffc
```
```
O
| H
√
P |
```
```
Table 4.1: Expression of Qa
```
```
YDC ( f )
fs
```
##### =

##### +∑∞

```
k =−∞
```
```
Regular part
︷ ︸︸ ︷
[
1 +
```
##### 1

##### M

##### M ∑− 1

```
m =1
```
```
δOm (. )
```
##### ]

```
O 0 δ ( f − kfs )
```
##### +

##### +∑∞

```
k ̸=0[ M ]
−∞
```
##### 1

##### M

##### [ M − 1

##### ∑

```
m =1
```
```
ζ − mkδmO
```
##### ]

```
O 0 δ ( f − k
fs
M
```
##### )

##### ︸ ︷︷ ︸

```
Spurious part
```
##### (4.2)

```
YAC ( f )
fs
```
##### =

##### +∑∞

```
k ̸=0[ M ]
−∞
```
##### 1

##### M

##### [ M − 1

##### ∑

```
m =1
```
```
ζ − mkδHm (. )
```
##### ]

##### H 0 (. ) X (. )

##### ︸ ︷︷ ︸

```
Spurious part
```
##### ∣

##### ∣

##### ∣

##### ∣

```
f − kfMs
```
##### +

##### ∑+∞

```
k =−∞
```
```
Regular part
︷ ︸︸ ︷
[
1 +
```
##### 1

##### M

##### M ∑− 1

```
m =1
```
```
δHm (. )
```
##### ]

##### H 0 (. ) X (. )

##### ∣

##### ∣

##### ∣

##### ∣

```
f − kfs
```
##### (4.3)

```
Where ζ = ej
```
(^2) _Mπ_
is the _Mth_ unitary root. The demonstration is detailed in
Appendix B. By reassembling (4.2) and (4.3), _Y_ ( _f_ )is written as a sum of a
regular part and a spurious part:
_Y_ ( _f_ ) = _Yregular_ ( _f_ ) + _Yspur_ ( _f_ ) (4.4)
The regular part is made up of replicas of the fundamental signal at multiple of
_fs_ and it corresponds to what would be obtained with a single ADC sampled
at _fs_. The spurious part consists of replicas at fractions of _fs_ and comes from
discrepancies between each channel. The spurious part of the DC component
_YDC_ appears as a line spectrum independent of the signal at fixed frequencies
_kfMs_.

### 4.5 Pairing between mismatches

Based on (2.39), the relative transfer function mismatch _δHm_ can be writ-
ten as a function of the gain, time-skew and bandwidth mismatch through a
logarithmic derivative:

```
δHm ( f ) = δgmQ 0 ( f ) + δtmQ 1 ( f ) + δfcmQ 2 ( f ) (4.5)
```

```
where
```
##### 

##### 

##### 

##### 

##### 

```
Q 0 ( f ) = 1
Q 1 ( f ) = j 2 πf Ts
Q 2 ( f ) =
```
```
jffc
1+ jffc
```
##### (4.6)

_Q_ 0 is a unit filter and is associtated to the gain mismatch. _Q_ 1 is a differentiator
and is associated to the time-skew mismatch. _Q_ 2 is a high pass filter and
is associated to the bandwidth mismatch. The advantage of (4.3) and (4.5)
is that gain, time-skew and bandwidth mismatches are aggregated in a single
mismatch _δHm_. (4.5) and (4.6) show that gain mismatch occurs on the real
part of _δHm_. Time-skew mismatch is frequency dependent and occurs on the
imaginary part of _δHm_. Bandwidth mismatch is frequency dependent and can
combine constructively or destructively with gain and time-skew mismatches.

#### 4.5.1 Spur power analysis

Let _x_ ( _t_ ) =

##### √

_P_ exp( _j_ 2 _πfot_ )be the input signal. Based on (4.3), _YAC_ spurs
appear at frequencies _fo_ + _kfMs_. The power of the _kth_ spur of _YAC_ is :

```
PkAC =
```
##### 1

##### M^2

##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

##### M ∑− 1

```
m =0
```
```
ζ − mkδmH ( fo )
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

```
2
| H ( fo )|^2 P (4.7)
```
Likewise, (4.2) gives _YDCkth_ spur power :

```
PkDC =
```
##### 1

##### M^2

##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

##### M ∑− 1

```
m =0
```
```
ζ − mkδmO
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

```
2
O^20 (4.8)
```
Let’s denote _Qa_ ( _fo_ )in (4.5) the filter associated to _a_ where _a_ stands for
either gain, time-skew or bandwidth. For the special case of offset which is
totally independent of the input signal, we define _Qo_ ( _f_ ) =| _H_ ( _fO_^0
_o_ )|

√
_P_. We note
_εam_ ∈ { _δgm, δtm, δfcm, δOm_ }the relative mismatch associated to _a_ and _Ca_ =
| _Qa_ |^2. Assuming mismatch _a_ is predominant, the _kth_ spur power is :

```
Pkspur =
```
```
Ca
M^2
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

##### M ∑− 1

```
m =0
```
```
ζ − mkεam
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

```
2
| H ( fo )|^2 P (4.9)
```
Fig. 4.6 and Table 4.2 compare some simulation results with (4.9) when using a
4 TI-ADCs with bandwidth mismatches. Considering a sinusoidal input, spurs
appear effectively at frequencies± _fo_ + _kMfs_ and their power match with (4.9).

#### 4.5.2 Dynamic specifications of TI-ADCs

The signal to the _kth_ spur ratio ( _SSRk_ ) referred to the TI-ADC output is defined
by:

```
SSRk =
```
```
| H ( fo )|^2 P
Pkspur
```
##### =

##### M^2

```
CaZa ( k )
```
##### (4.10)


```
Frequency Spur power
according to (4.9)
[dB]
```
```
Simulated spur
power [dB]
```
```
− fo + f 2 s -64.81 -64.81
```
```
fo − f 4 s -72.62 -72.71
```
```
− fo + 3 f 4 s -72.62 -72.71
```
Table 4.2: Simulation results of a 4 TI-ADC with bandwidth mismatch for an
input signal _x_ ( _t_ ) = 1_._ 5 sin(2 _πfot_ ), _fo_ = 146_._ 29 MHz and _fs_ = 320MHz.
[ _fcofc_ 1 _fc_ 2 _fc_ 3 ] = [4.01 3.94 4.12 3.86] GHz.

```
where Za ( k ) = Za ( M − k ) =
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

##### M ∑− 1

```
m =0
```
```
ζ − mkεam
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

```
2
(4.11)
```
The Spurious-Free-Dynamic Range (SFDR) of a TI-ADC is derived from (4.10)
as :

```
SF DR = min
k =1 ,..., ⌊ M 2 ⌋
```
```
SSRk (4.12)
```
```
−180 0 20 40 60 80 100 120 140 160
```
```
−160
```
```
−140
```
```
−120
```
```
−100
```
```
−80
```
```
−60
```
```
−40
```
```
−20
```
```
0
```
```
Frequency MHz
```
```
− fo + f 2 s fo − f 4 s − fo +^3 f 4 s fo f 2 s
```
```
Spurs due to bandwidth mismatch
```
```
Fundamental component
```
```
Power in dB
```
Figure 4.6: Output spectrum of a 4 TI-ADCs with bandwidth mismatch for
an input signal _x_ ( _t_ ) = 1_._ 5 sin(2 _πfot_ ), _fo_ = 146_._ 29 MHz and _fs_ = 320MHz.
[ _fcofc_ 1 _fc_ 2 _fc_ 3 ] = [4.07 3.80 3.98 3.85] GHz.

### 4.6 Probabilistic Description of Mismatches

#### 4.6.1 Motivation

Device mismatches are caused by Process, Voltage and Tempretaure (PVT) vari-
ations and are commonly described by random variables normally distributed.


```
Ts = 20ns
```
```
Time-skew τs
```
```
y 1
```
```
y 2
```
```
13 inverters
```
```
Figure 4.7: Two chains of 13 inverters clocked at 50 MHz in 65 nm process
```
For example, Fig. 4.7 represents the clock distribution circuitry for 2 chan-
nels in 65 nm process. The original clock has a frequency of 50 MHz. Ideally,
the outputs _y_ 1 and _y_ 2 should be identical since both channels have the same
input. However, due to PVT variations this is not the case. Fig. 4.8 shows the
distribution of delay mismatch between the two outputs obtained by running
Monte Carlo simulations. The standard deviation of this time-skew mismatch
is approximately 30 ps which represents 0_._ 15 % of the clock period.

To understand it, let’s consider a simple rough model of the CMOS inverter
delay of Fig. 4.9 [61]:

```
tinv =
```
```
VddCload
I
```
##### =

```
CloadVdd
μCoxWL ( Vdd − VT )
```
##### (4.13)

This delay is function of the inverter load _Cload_ , supply voltage _VDD_ and the
transistor threshold voltage _VT_ which depends also of the temperature _T_. Any
variation of these parameters from one inverter to another will result in delay
mismatch at the output of the chain. Thus, using this rough model and con-
sidering _Ninv_ inverters per branch, time-skew mismatch can be modeled by a

gaussian variable _δtinv_ ∼N

##### (

##### 0 ,

##### √

```
NinvσTinvs
```
##### )

```
with σinv given by:
```
```
σinv ≃ tinv
```
##### (∆ C

```
load
Cload
−
VT
VDD ( VDD − VT )
∆ VDD +
1
VDD − VT
∆ VT
```
##### )

```
(4.14)
```
More generally we are going to consider that gain, time-skew, bandwidth and
offset mismatches are random. Since these mismatches are responsible for chan-
nel mismatch errors, it is convenient to rely on a probabilistic characterization
of the gain, offset, time-skew and bandwidth mismatches. As a consequence, the
SFDR is modeled by a statistical distribution related to the standard deviation
_σa_ of a specific mismatch as in [57].


```
−300^0 −200 −100 0 100 200 300
```
```
5
```
```
10
```
```
15
```
```
20
```
```
25
```
```
30
```
```
35
```
```
40
```
```
45
```
```
50
```
```
Time-skew in ps
```
```
Number of occurrences
```
Figure 4.8: Time-skew mismatch between two channel of 13 inverters in 65 nm
process at a frequency of 50 MHz

```
Cload
```
##### IN I OUT

```
Vdd
```
```
Figure 4.9: Typical CMOS inverter
```
```
Readily, εam = σaξam with ξam ∼N(0 , 1). (4.11) becomes :
```
```
Za ( k ) = σ^2 a
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

##### M ∑− 1

```
m =0
```
```
ζ − mkξam
```
##### ∣

##### ∣

##### ∣

##### ∣

##### ∣

```
2
= σ^2 aSa ( k ) (4.15)
```
#### 4.6.2 Probability Density Function of SFDR and THD

In the previous sections, we saw that channel mismatches can be described by
random variables normally distributed. As the SFDR is also function of these
mismatches, it is important to rely on a probabilistic description of the SFDR.
In the following analysis, we are going to consider that mismatch _a_ is predomi-
nant where _a_ stands for either gain, time-skew, bandwidth of offset mismatch.
In section 4.6.2, we will provide a general framework to describe the PDF of
all mismatches including bandwidth. Therefore this will extends the work pre-
sented in [57] where bandwidth mismatch was not considered.

```
In practice, the analog designer is not only interested in PDF of the SFDR.
```

Indeed he also wants to establish safe margins for his design by looking for the
probability that the SFDR is greater than the targeted value. Therefore using an
analogy to the usual yield, we will introduce a robustness criterion _SF DR_ ( _η_ )
which states that the SFDR remains higher than the threshold value with a
probability _η_. Therefore this extends the work presented in [58][56] where only
mean value were determined.

**Probability Density Function of SFDR**

The SFDR is defined as the ratio of the fundamental signal to the worst spurious.
So we have:

```
SF DR = 10 log 10
```
```
[ Psignal
Pmaxspur
```
##### ]

```
= 10 log 10
```
##### [

```
max
k =1 ,..., ⌊ M 2 ⌋
```
```
SSRk
```
##### ]

```
= 10 log 10
```
##### [ M 2

```
σ^2 aCa max k =1 ,..., ⌊ M 2 ⌋ Sa ( k )
```
##### ]

```
= 10 log 10
```
##### [ M 2

```
σ^2 aCaSmax
```
##### ]

```
= F ( Smax )
```
##### (4.16)

In (4.16), the function _F_ is monotone. Let’s call _fmax_ the PDF of _Smax_
which is calculated in Appendix. C.2. Using (4.16) and a variable change, we
find that for _M_ odd:

```
p ( SF DR ) =
```
##### 1

##### F ′

##### [

##### F −^1 ( SF DR )

```
] fmax
```
##### (

##### F −^1 ( SF DR )

##### )

```
= α
```
##### M − 1

##### 2

```
se − s (1− e − s )
```
```
M − 3
2
```
##### ∣

##### ∣

##### ∣

_s_ = _σ_ (^2) _aMCa_ 10 −
_SF DR_ 10

##### (4.17)

With _α_ =−log 10 10 and _Ca_ =| _Qa_ |^2 is a frequency dependent coefficient depending
of the mismatch analyzed. For _M_ even, the PDF of the SFDR is given by:

_p_ ( _SF DR_ ) = _αs_ (1− _e_ − _s_ )

##### M − 24 [ M − 2

##### 2

```
e − serf (
```
```
s
2
```
##### )+

##### 1

##### √

```
2 πs
```
```
e − s (1− e −
```
```
s 2
)
```
##### ]∣

##### ∣

##### ∣

_s_ = _σ_ 2 _M
aCa_
10 − _SF DR_^10
(4.18)
With _erf_ the Gauss error function.
Fig. 4.10, 4.11 and 4.12 compare the above PDF with simulation results of a
two-TIADCs with gain, time-skew and bandwidth mismatches. We can notice
that the statistical distribution of SFDR matches pretty well with the analytical
PDF calculated above.


(^030405060708090100)
500
1000
1500
2000
2500
SFDR in [dB]
Number of occurences
By simulation
By formula
Figure 4.10: PDF of a two-channel TI-ADCs with a gain mismatch of 1 % and
with a input sinusoid of amplitude 1 V
(^0405060708090)
500
1000
1500
2000
2500
3000
3500
4000
4500
5000
SFDR in dB
Number of occurences
By simulation
By formula
Figure 4.11: PDF of a two-channel TI-ADCs with a time-skew mismatch of 1 %,
a sampling frequency of 320 MHz and with a input sinusoid of amplitude 1 V
and a frequency of 137 MHz


(^030405060708090)
500
1000
1500
2000
2500
3000
3500
4000
4500
5000
SFDR in dB
Number of occurences
By simulation
By formula
Figure 4.12: PDF of a two-channel TI-ADCs with a bandwidth mismatch of
1 %, a sampling frequency of 320 MHz and with a input sinusoid of amplitude
1 V, a frequency of 137 MHz and a cutoff frequency of 160 MHz


#### 4.6.3 Cumulative Density Function of SFDR

As the SFDR is function of the random variables _Sa_ ( _k_ ), it is also a random
variable whose dispersion depends on standard deviation of mismatches _σa_.
Therefore using an analogy to the usual _yield_ , we introduce the robustness
criterion _SF DR_ ( _η_ ), that states the SFDR remains higher than this threshold
value with a probability 1 − _η_. For _M_ odd :

```
η = P
```
##### (

```
SF DR < SF DR ( η )
```
##### )

##### = 1−

```
M − 21
∏
```
```
k =1
```
##### P

##### (

##### 2

##### M

```
Sa ( k ) <
```
##### 2 M

```
σa^2 CaSF DR ( η )
```
##### )

```
η = 1−
```
##### [

##### F 2

##### (

##### 2 M

```
σa^2 CaSF DR ( η )
```
##### )] M 2 −^1

##### (4.19)

_F_ 2 ( _s_ ) = 1− _e_ −
_s_ 2
is the Cumulative Density Function of the two degrees of
freedom Chi-square variables _M_^2 _Sa_ ( _k_ ), which are independent each other for
_k_ ∈{ 1 _, ...,_ ⌊ _M_ 2 ⌋}[57].
Inverting (4.19) with respect to _SF DR_ ( _η_ )gives :

```
SF DRdB ( η ) =−10 log 10
```
```
Caσ^2 a
M
```
```
−10 log 10 K ( η, M ) (4.20)
```
With _K_ ( _η, M_ )≃ln

##### (

```
M − 1
2 η
```
##### )

. (4.20) still holds numerically for M even. It states

the SFDR remains higher than the threshold value _SF DRdB_ ( _η_ )with the proba-
bility 1 − _η_ allowing to control the reliability of any mismatch calibration process
which is not possible when only mean values are considered [56] [57] [58].

Fig. 4.13 shows the SFDR law as a function of _M_ , the mismatch type and
its standard deviation. Intrinsic channel error dispersions introduced by device
mismatches make the TI-ADC architecture not compatible with applications
requiring high SFDR in the order of 90 dB.

Indeed, based on [62], the bandwidth mismatch is about 35 000 ppm in
0_._ 13 μm process. Assuming _fs_ = 320MHz, _f_ 0 = 146_._ 29 MHz, _fc_ = 4GHz and

_M_ = 4, results in
_C_^1 _a_ √ _/_^2 _σa
M_ = 640 ppm. Substituting this value in (4.20) and
considering _η_ =1e−3 gives a low SFDR of 55 dB.

If we take again the time-skew mismatch of 0_._ 15 % i.e 1 500 ppm obtained
in section 4.6.1 with a clock frequency of 50 MHz in 65 nm. And if we assume
an interleaving factor of 4 and a signal frequency of 10 MHz, we obtain a low
SFDR of 50 dB.

These two examples emphasize the necessity of calibrating TI-ADC when
high linearity is needed. Targetting 90 dB SFDR, the initial mismatches should
be reduced at least to two orders of magnitude. Tab. 4.3 summarizes the
matching requirements for the four type of mismatches.


```
C^1 a √ /^2 σa
M in ppm
```
```
SFDR in dB
```
```
Figure 4.13: SFDR distortion law
```
- Gain Time-skew Bandwidth Offset

```
Accuracy in
ppm
```
##### 20 7 540 120

Table 4.3: Matching needed to reach the desired SFDR of 90 dB in 99_._ 9 % of
cases with a 4 TI-ADCs, an input signal _x_ ( _t_ ) = 1_._ 5 sin(2 _πf_ 0 _t_ ), _f_ 0 = 146_._ 29 MHz
and _fs_ = 320MHz


### 4.7 Integral and Differential Non-Linearities

The DNL of code _m_ of a M TI-ADCs is the average of DNL of different sub-
ADCs:

```
DN L ( m ) =
```
##### 1

##### M

##### N ∑− 1

```
i =0
```
```
DN Li ( m ) (4.21)
```
Where _DN Li_ ( _m_ )is the DNL of code _m_ of the _ith_ ADC. As seen in formula
(2.38), the INL/DNL of each sub ADC can be written as a sum of capaci-
tor mismatch which can be modeled by random variable normally distributed.
Therefore the DNL of each sub-ADC can be considered also as gaussian variable
and the variance of the DNL of the overall TI-ADC is:

```
σ^2 ( DN L ) =
```
##### 1

##### M^2

##### M ∑− 1

```
i =0
```
```
σ^2 ( DN Li ) (4.22)
```
(4.22) shows that DNL errors of the overall TI-ADCs is lower than the DNL
errors of each of the M sub-ADCs. The same result can be obtained with INL.


### 4.8 Conclusion

In this chapter we have derived a deterministic model describing simultaneously
the gain, time-skew, bandwidth and offset mismatches in a TI-ADC. A prob-
abilistic law linking the SFDR to mismatch requirements has been provided.
Numerical results show that initial mismatches must be reduced significantly
by two orders of magnitude to obtain substantial SFDR in the order of 90 dB.
It leads to consider a fully digital calibration mechanism with two purposes:
mismatch estimation and compensation for which the following problems are
anticipated.

On the one hand, the complexity level of the estimation phase depends on
prior knowledge on the input signal, whether these are known sinusoids or un-
known band-limited signals with known power spectral density. Since it works
sporadically and requires flexibility, this block is preferably implemented in soft-
ware.

On the other hand, the compensation phase is obvious for gain and off-
set, whereas the frequency dependency of time-skew and bandwidth makes the
associated filtering problem challenging. This blocks can be implemented in
hardware as it works at the sampling rate and is settled once and for all.

The next chapter will focus on the digital calibration algorithm we propose
to cancel the effects of channel mismatch errors.



## Chapter 5

# Proposed Digital

# Calibration Scheme

### 5.1 Introduction and State of art

In the previous chapters, a lot of effort has been made to model a ADCs. In
chapter 2, the differential equations governing the dynamics of non ideal S/H
circuits were derived and then solved. This substantial effort of modeling has
allowed us to identify precisely the analog variables which were responsible for
distortion. Chapter 3 has completed this analysis with the statistical description
of noise in ADCs. Then in chapter 4, this model of a single ADC has been ex-
tended to the case of time interleaved architecture in function of gain, time-skew
and bandwidth mismatches all together. We demonstrated that these discrep-
ancies between sub ADCs lead to the degradation of dynamic performances such
as SFDR and should be mitigated.

There are two possible ways to deal with channel mismatches. The first is
to complexify the analog circuit design of the ADC in order to reduce the mag-
nitude of the original mismatches at the cost of more power consumption and
area. But this increases the time-to-market of the ADC. The second solution is
to alleviate the design and to correct the errors with a calibration technique as
we are going to do in this chapter. Depending of the nature of the input signal,
calibration techniques can be classified into foreground and background.

Foreground techniques interrupt the normal ADC operation by injecting
a known signal to perform calibration and they are not suitable for applica-
tions such as communications where the ADC should be always running. In
background calibration techniques, the ADC operation continues when the cal-
ibration is being performed. The mismatches are continuously estimated and
corrected. These techniques can be subdivided into semiblind and blind. Semi-
blind background calibration techniques combine the input signal with a test
signal that will be used for the calibration [5]. In blind background calibration
techniques, no test signal is used [6]. Blind background calibration techniques
are the most difficult to design because they should track and adjust to the
changing operation conditions of ADCs in demanding environments with rapidly


changing temperatures. In addition, they should work with no informations or
with little a priori informations on the input signal such as statistics.

When the calibration uses a feedback to the analog front-end of the ADC, it is
a mixed signal calibration [7][8]. When it is done entirely in the digital domain,
the calibration is said to be fully digital [9][10][5]. Mixed signal calibration
techniques are popular in current TI-ADCs chips but fully digital calibrations
are more and more desired because they require no custom redesign of the analog
front-end of the ADC [8].
Several works have been done on correcting the gain, time-skew and offset
mismatches in TI-ADCs [10] [7] [13] [6] [14] [15] [16], but little work has been
done on bandwidth mismatches. In [5] [17] [18], some bandwidth mismatch cal-
ibrations are proposed for two channels ADCs but they dont take into account
the time-skew and gain mismatch. Indeed bandwidth mismatch is frequency
dependent and is likely to combine constructively or destructively with time-
skew and gain mismatch as demonstrated in chapter 4. Therefore these three
mismatches should be treated jointly for more optimality. In [19], a calibration
method for gain, time-skew and bandwidth mismatches using a feedforward
equalizer is proposed, but the algorithm takes a long time to converge. In [20],
a calibration of frequency response mismatch is proposed by modeling transfer
function as polynomial with variable order differentiators and coefficients. This
was done for only two channels and the decomposition in differentiator filters is
more accurate for time-skew mismatch correction than for bandwidth mismatch.

To overcome these limitations of the state of art, we propose in this chapter
a fully digital adaptive and blind background calibration of channel mismatches
in TI-ADCs. The contribution of this chapter is:

- a simultaneously and blind estimation of gain, time-skew and bandwidth
    mismatches. The estimation of all mismatches is achieved with less than
    10-K samples with an accuracy of 98%, 94% and 88% for gain, time-skew
    and bandwidth.
- a fully digital correction of gain, time-skew, bandwidth and offset mis-
    matches. The linearity of the TI-ADCs can be improved by almost 40 dB.
- a calibration that can be applied to any interleaved factor.

### 5.2 Estimation of channel mismatches

Before correcting channel mismatch errors, the mismatches should be estimated.
To do it, we choose channel 0 as reference channel and then apply a low-pass and
a fractional delay filter to this reference channel to obtain some samples that will
be compared to the output of non reference channels allowing the identification
of channel mismatches. This is done blindly i.e without a test signal so that the
ADC can keep running while estimation is being processed. We only assume
that the input signal is bandlimited and Wide Sense Stationary (WSS) which
is relevant for a communication system.


```
HM − 1
```
```
x ( t )
```
```
H 1
```
- _H_ 0

```
?
```
```
?M ADC^0
```
```
ADC 1
?M
```
```
y 0
```
```
ADCM − 1
?M
```
(^6) M
?
+?
_z_ −^1
?
+?
(^6) M-
(^6) M-
_y_ 1
_z_ −^1
_z_ −^1 -
?
_z_ −^1

- _y_

```
yM − 1
```
```
Multiplexing
y 0
```
```
y 1
```
```
yM − 1
```
```
Figure 5.1: Time-Interleaved ADCs
```
Let’s consider the M TI-ADC of Fig. 5.1 and an unknown input signal _x_ ( _t_ )
bandlimited and WSS. Let’s call _ym_ the signal just after the ADC of channel
_m_ as represented on Fig. 5.1:

```
ym [ k ] = ( hm⋆ x )( kM Ts − mTs ) + wm [ k ]
= xm [ k ] + wm [ k ]
```
##### (5.1)

_wm_ is the total noise on channel _m_ which is assumed to be white and gaussian
[63]. The DTFT _Xm_ ( _f_ )of the signal _xm_ in (5.1) consists of replicas of the
fundamental signal at shifted frequencies _f_ − _kfMs_ as shown on Fig. 5.2:

```
Xm ( f ) =
```
##### ∑∞

```
k
```
```
exp(− j 2 π (. ) mTs )
```
##### [

```
1 + δHm (. )
```
##### ]

```
H 0 (. ) X (. )
```
##### ∣

##### ∣

##### ∣

```
f − kfMs
```
```
(5.2)
```
If we apply a lowpass filter _hLP_ to _ym_ we can obtain a signal _zm_ which is alias
free as shown on Fig. 5.2:

```
zm [ k ] = ( hLP⋆ xm )( kTs )
︸ ︷︷ ︸
xm [ k ]
```
```
+ ( hLP⋆ wm )( kTs )
︸ ︷︷ ︸
bm [ k ]
```
##### (5.3)

The noise _bm_ in (5.3) is gaussian and bandlimited and the DTFT _Xm_ of the
signal _xm_ in (5.3) has no alias (Fig. 5.2):

```
Xm ( f ) = exp(− j 2 πf mTs )
```
##### [

```
1 + δHm ( f )
```
##### ]

```
H 0 ( f ) X ( f ) (5.4)
```
Let’s call _hmdl_ , the delay filter whose transfer function is _Hdlm_ ( _f_ ) = exp(− _j_ 2 _πf mTs_ ).
_hmdl_ has a rational fractional delay _Mm_ because on each channel the sampling pe-
riod is _M Ts_ and _m < M_. Using (5.3) and (5.4), let’s define the signal∆ _zm_
by:

```
∆ zm [ k ] = zm [ k ]−( hmdl⋆ z 0 )[ k ]
```
```
=
```
##### (

```
hLP⋆ hmdl⋆ δhm⋆ h 0 ⋆ x
```
##### )

```
[ k ]
```
```
+ bm [ k ]−( hmdl⋆ b 0 )[ k ]
```
##### (5.5)


```
Figure 5.2: Spectrum of the mth ADC output
```
Equations (5.6) and (5.7) remind the expression of the transfer function
mismatch in function of the gain, time-skew and bandwidth mismatches and
also the expressions of filters _Q_ 0 , _Q_ 1 and _Q_ 2.

```
δHm ( f ) = δgmQ 0 ( f ) + δtmQ 1 ( f ) + δfcmQ 2 ( f ) (5.6)
```
```
where
```
##### 

##### 

##### 

##### 

##### 

```
Q 0 ( f ) = 1
Q 1 ( f ) = j 2 πf Ts
Q 2 ( f ) =
```
```
jffc
1+ jffc
```
##### (5.7)

Using (5.5) and (5.6) we can estimate adaptively the gain, the time-skew
and the bandwidth mismatches of each channel _m_ with the structure of Fig.
5.3.
Let’s denote _θθθm_ = [ _δgmδτmδfcm_ ] _t_ the mismatch vector of channel _m_ , _θ_ ˆ _θθ_ the
estimated value of mismatches,∆ˆ _zm_ = ( _δh_ ˆ _m⋆ z_ 0 )with _δh_ ˆ _m_ the estimated
transfer function mismatch calculated through (5.6). Let’s _e_ ( _θθθ, k_ )be the error

function used to adaptˆ _θθθ_ as shown Fig. 5.3:

```
e ( θθθ, k ) = ∆ zm [ k ]−∆ z ˆ m [ k ]
```
```
=
```
##### (

```
hLP⋆ hmdl⋆ { δhm − δh ˆ m } ⋆ h 0 ⋆ x
```
##### )

```
[ k ]
```
```
− bm [ k ]−( hmdl⋆ b 0 )[ k ]
```
##### (5.8)

Applying the gradient descent algorithm, we find the iteration to use:

```
θθ ˆ θm ( k + 1) = θθ ˆ θm ( k + 1)− μμμe (ˆ θθθm, k )▽ θθ ˆ θ
me (
ˆ θθθm, k ) (5.9)
```
Where _μμμ_ is the iteration step vector and▽ˆ _θθθme_ (ˆ _θθθm, k_ )is the gradient of the error
function given by:

```
▽ˆ θθθme ( θ ˆ θθm, k ) =
```
##### [

```
( Q 0 ⋆ z 0 )[ k ] ( Q 1 ⋆ z 0 )[ k ] ( Q 2 ⋆ z 0 )[ k ]
```
```
] t
(5.10)
```

##### -

```
δm ˆ g δm ˆ τ δm ˆ fc
```
```
Q 1 ( z ) Q 2 ( z )
```
##### 

##### 

##### 6

##### - + 

##### 6

##### 

##### 

##### +

##### 6

##### 

##### 

##### +

#####  7 7

```
zm ( k )
```
```
z 0 ( k )
```
```
∆ zm
− −
```
```
e ( θθθm, k )
```
```
∆ˆ zm
```
```
HLP ( z )
```
- _HLP_ ( _z_ )

```
ym ( k )
```
```
y 0 ( k )
```
```
Q 0 ( z )
```
##### -

- _Hmdl_ ( _z_ )

##### -

```
δh ˆ m
```
```
Figure 5.3: Adaptive filtering structure
```
- (^6) M - _HLP_ - _z_ − _m_ - ?M -
Figure 5.4: Multirate fractional rational delay _m/M_

### 5.3 Compensation of channel mismatch errors

Once mismatches have been estimated, they should be corrected. To do
it, we use a matrix approach first introduced in [5] for the compensation of
only bandwidth mismatch in the specific case of a 2-channels TI-ADCs that we
extend for gain, time-skew and bandwidth mismatches and for any interleaved
factor _M_. Let’s use the following notations:

- **Y** = [ _Y_ 0 ( _f_ ) _...YM_ − 1 ( _f_ )] _t_ with _Ym_ ( _f_ )the output of channel _m_ of the TI-
    ADCs of Fig. 5.1 in the frequency domain.
- **V** the MxM unitary matrix given by _VVVmk_ = _ζ_ − _mk_
- **∆** the MxM matrix given by∆∆∆ _mk_ = _ζ_ − _mkδHm_ (_._ )

##### ∣

##### ∣

##### ∣

```
f − kfMs
```
- **D** the Mx1 vector given by: **D** _k_ = _H_ 0 (_._ ) _X_ (_._ )

##### ∣

##### ∣

##### ∣

```
f − kfMs
```
##### .

```
The DTFT Ym of the ym of channel m can be written as:
```
```
Ym ( f ) =
1
M
Λ( f )
```
##### M ∑− 1

```
k =0
```
```
ζ − mk
```
##### [

```
1 + δHm (. )
```
##### ]

```
H 0 (. ) X (. )
```
##### ∣

##### ∣

##### ∣

```
f − kfMs
```
```
(5.11)
```

```
Digital
Correction
```
```
Estimation
```
```
TI-ADCs -
```
-
    -

```
}
```
```
samples corrected
```
```
Figure 5.5: Principle of the fully digital calibration.
```
```
Based on (5.11), the output vector of the TI-ADCs is:
```
##### Y =

##### Λ

##### M

##### [ V + ∆ ] D =

##### Λ

##### M

##### [

##### I M +

##### 1

##### M

##### ∆V †

##### ]

##### VD (5.12)

In (5.12), **I** _M_ is the MxM identity matrix and **V** †is the hermitian transpose of
**V**. In the ideal case, there are no mismatches, **∆** = **0** , and the ideal output is:

```
Y ideal =
```
##### Λ

##### M

##### VD (5.13)

In practice, device mismatches are inherent to any manufacturing process and
result in channel mismatch errors ( **∆** ̸= **0** ). The actual output can be written
as:

##### Y =

##### [

##### I M +

##### 1

##### M

##### ∆V †

##### ]

```
Y ideal (5.14)
```
To calibrate the TI-ADCs, the effect of mismatches should be canceled in (5.14)
such that the corrected output **Y** _c_ becomes almost equal to **Y** _ideal_ :

```
Y c =
```
##### [

```
I M +
1
M
∆V †
```
##### ]− 1

```
Y ≃
```
##### [

```
I M −
1
M
∆V †
```
##### ]

```
Y = FY (5.15)
```
In (5.15), **F** contains the set of filters that should be applied to the output of
the TI-ADCs for calibration. The approximation of (5.15) is obtained using the
Taylor expansion for matrix since the mismatches in **∆** are small.

#### 5.3.1 Particular case M=2

For the particular case of two channels, the matrix **F** of compensation filters
obtained from (5.15) are given in (5.16). The associated compensation structure
is shown on Fig. 5.6. One should notice that only channel 1 is calibrated since
channel 0 is the reference channel.





```
F 00 ( f ) = 1 F 01 ( f ) = 0
F 10 ( f ) =−^12
```
##### [

```
δH 1 ( f )− δH 1 ( f − f 2 s )
```
##### ]

```
F 11 ( f ) = 1−^12
```
##### [

```
δH 1 ( f ) + δH 1 ( f − f 2 s )
```
##### ] (5.16)


##### + -

##### 

##### ?

##### F 10

##### ?

##### -

##### -

```
y 0
```
_y_ (^1) _c
y_ 0
_y_ 1
_F_ 11
Figure 5.6: Compensation structure for M=2
With this particular case of two channels, we are going to analyze analytically
and by simulation the performance of this technique by evaluating the spur
power before and after calibration. We will consider an input signal consisting of
two unit sinusoids at frequencies 40 MHz and 80 MHz sampled at _fs_ = 320MHz.
The spectrum will be observed in the interval [0 _fs_ ].

#### 5.3.2 Before calibration

The DTFT _Y_ 0 and _Y_ 1 of the two outputs _y_ 0 and _y_ 1 are given by:

```
Y 0 ( f ) =
```
##### 1

##### 2

##### [

```
H 0 ( f ) X ( f ) + H 0 ( f ′) X ( f ′)
```
##### ]

```
Y 1 ( f ) =
```
##### 1

##### 2

##### [{

```
1 + δH ( f )
```
##### }

```
H 0 ( f ) X ( f )−{1 + δH ( f ′)} H 0 ( f ′) X ( f ′)
```
##### ] (5.17)

To simplify notations in (5.17), _f_ ′= _f_ − _f_ 2 _s_. The output of the TI-ADCs is
obtained by summing the two outputs:

```
Y ( f ) = Y 0 ( f ) + Y 1 ( f )
```
```
=
```
##### [

##### 1 +

##### 1

##### 2

```
δH ( f )
```
##### ]

```
H 0 ( f ) X ( f )
︸ ︷︷ ︸
F undamental
```
##### −

##### 1

##### 2

```
δH ( f ′) H 0 ( f ′) X ( f ′)
︸ ︷︷ ︸
spurious at f ′= f − f 2 s
```
##### (5.18)

From (5.18), we see that channel mismatches create a disturbing component
which occurs at shifted frequency _f_ − _f_ 2 _s_. When there no mismatches, _δH_ ( _f_ ) = 0
and the ideal output is:

```
Y ( f ) = H 0 ( f ) X ( f ) (5.19)
```
#### 5.3.3 After calibration

To reduce the magnitude of the disturbing component in (5.18), _Y_ 0 will be
considered as the reference channel and _Y_ 1 will be calibrated. Let’s apply the
filters _F_ 10 and _F_ 11 respectively to _Y_ 0 and _Y_ 1 in order to obtain the calibrated
signal _Y_ 1 _cal_ :

```
Y 1 cal ( f ) = F 10 ( f ) Y 0 ( f ) + F 11 Y 1 ( f ) (5.20)
```

With _F_ 10 and _F_ 11 defined in (5.16). Now the serial output _Y_ can be calcu-
lated again as:

```
Y ( f ) = Y 0 ( f ) + Y 1 cal ( f )
```
##### =

```
F undamental
︷[ ︸︸ ︷
1 −
```
##### 1

##### 4

```
δH ( f )
```
##### (

```
δH ( f ) + δH ( f ′)
```
##### )]

```
H 0 ( f ) X ( f )
```
```
+
```
##### 1

##### 4

##### [

```
δH ( f ′)
```
##### (

```
δH ( f ) + δH ( f ′)
```
##### )]

```
H 0 ( f ′) X ( f ′)
︸ ︷︷ ︸
Spurious at f ′= f − f 2 s
```
##### (5.21)

From (5.18) and (5.21), we see that the mismatches have been reduced from the
first order to the second order. Now the actual output in (5.21) is close to the
ideal output obtained in (5.19).

### 5.4 Simulation results with a two-channel ADCs

We consider WiFI IEEE 802.11.ac with a bandwidth up to 160 MHz imple-
mented with an IQ architecture. Each base-band signal has 80 MHz bandwidth
oversampled at 340 MHz with a 12-bits 2-TI-ADCs. The gain, the time-skew
and the cutoff frequency of the first ADC is _G_ 0 = 1, _τ_ 0 = 1psand _fc_ 0 = _f_ 2 _s_. The
gain, the time-skew and the bandwidth mismatch are respectively _δg_ 1 = 1%,
_δτ_ 1 = 1% and _δfc_ 1 = 2%. The estimation uses the adaptive filtering structure
of Fig. 5.3 and the compensation uses the structure of Fig. 5.6.

Filters _HLP_ , _Hmdl_ , _Q_ 0 , _Q_ 1 , _Q_ 2 , _F_ 10 and _F_ 11 are implemented with FIRs. The
impulse response of _HLP_ is obtained by applying a Kaiser window to its inverse
DTFT. The fractional delay filter _Hmdl_ is obtained from _HLP_ with the multirate
structure of Fig. 5.4 since it has a rational fractional delay [64]. Filters _Q_ 0 , _Q_ 1
and _Q_ 2 are designed with the sampling frequency technique since they should
have a predefined magnitude and phase response specified by (5.7). _F_ 10 and _F_ 11
of (5.16) can be obtained from _Q_ 0 , _Q_ 1 and _Q_ 2 with (5.6). The iteration step
vector is set to _μμμ_ = [1e−5 3e−5 5e− 6 ]in order to have a good precision with
a suitable convergence.

Tab. 5.1 presents simulation results before and after calibration with 2 unit
sinusoids at frequencies 40 MHz and 80 MHz. For only gain mismatches, the
SFDR is improved by 41 dB. For only time-skew mismatch the SFDR is im-
proved by 40 dB and for bandwidth mismatch the SFDR is improved by 32 dB.
Considering all mismatches, the SFDR can be improved by 40 dB and Fig. 5.8
shows the spectrum before and after calibration. Fig. 5.7 presents the con-
vergence of the mismatch estimation with the number of samples. Globally
we need 10K samplesto estimate all mismatches. The estimation accuracy is
98%, 94% and 99% respectively for gain, time-skew and bandwidth mismatches.


```
Mismatch Before
calibration After calibration
```
```
Improvement
```
Only gain 46 87 41
Only time-skew 43 83 40
Only bandwidth 48 80 32
All mismatches 38 80 42

```
Table 5.1: SFDR in dB for a 2-channel at 40 MHz and 80 MHz
```

```
Number of K-samples
```
```
0 5 10 15 20
```
```
Estimated mismatches in %
```
```
-1.5
```
```
-1
```
```
-0.5
```
```
0
```
```
0.5
```
```
1
```
```
1.5
```
```
2
```
```
Convergence of Estimation
```
```
estimated gain mismatch
exact gain mismatch
estimated skew mismatch
exact skew
estimated bandwidth mismatch
exact bandwidth
```
```
Figure 5.7: Simulation of the Convergence of mismatch estimation
```
```
Frequency in MHz
```
```
0 50 100 150
```
Magnitude in dB

```
-180
```
```
-160
```
```
-140
```
```
-120
```
```
-100
```
```
-80
```
```
-60
```
```
-40
```
```
-20
```
```
0
```
```
Before Calibration
```
```
Frequency in MHz
```
```
0 50 100 150
```
```
Magnitude in dB
```
```
-180
```
```
-160
```
```
-140
```
```
-120
```
```
-100
```
```
-80
```
```
-60
```
```
-40
```
```
-20
```
```
0
```
```
After Calibration
```
```
Figure 5.8: Simulation of the output spectrum before and after calibration
```

(^45020406080100120140160)
50
55
60
65
70
75
80
85
90
Frequency in MHz
SFDR in dB
Before calibration
After Calibration
Figure 5.9: SFDR before and after correction with a two-channel TI-ADCs with
1% gain mismatch. The sampling frequency is 340 MHz.

### 5.5 Impact of the signal bandwidth

Now we can analyze the performances of the algorithm in function of the signal
bandwidth. For this purpose we are going to do several simulations for different
signal bandwidths ([0 _f_ 2 _s_ ]). The results are shown on Fig. 5.9, 5.10, 5.11 and
5.12 respectively for gain (1%), time-skew(-1%), bandwidth(2%) and all mis-
matches. We notice that for gain mismatches, the correction is constant with
the signal bandwidth. That is normal because gain mismatch is independent of
the frequency. Time-skew and bandwidth mismatches are frequency dependent
and we see that the performances of the calibration decrease with the signal
bandwidth and around the nyquist frequency an important loss appears. When
all the mismatches are present the same effect is visible in function of the signal
bandwidth. This phenomena has two explanations. One one hand it is due to
the fact that when the bandwidth of the signal increases, the bandwidth where
there are no alias decreases and so the estimation is done on a signal which is
very slow. Because the signal is slow the errors due to timing mismatches (time-
skew and bandwidth) are small and it becomes difficult to identify them. On
the other hand the transfer function mismatch is a high pass filter as we can see
on Fig. 5.13. When the input signal bandwidth increases, the transfer function
mismatch incrases and the approximation of (5.15) becomes less accurate.


(^30020406080100120140160)
40
50
60
70
80
90
100
110
Frequency in MHz
SFDR in dB
Before calibration
After Calibration
Figure 5.10: SFDR before and after correction with a two-channel TI-ADCs
with -1% time-skew mismatch. The sampling frequency is 340 MHz.
(^40020406080100120140160)
50
60
70
80
90
100
110
Frequency in MHz
SFDR in dB
Before calibration
After Calibration
Figure 5.11: SFDR before and after correction with a two-channel TI-ADCs
with 2% bandwidth mismatch. The sampling frequency is 340 MHz.


(^30020406080100120140160)
35
40
45
50
55
60
65
70
75
80
Frequency in MHz
SFDR in dB
Before calibration
After Calibration
Figure 5.12: SFDR before and after correction with a two-channel TI-ADCs with
1% gain mismatch, -1% time-skew mismatch and 2% bandwidth mismatch. The
sampling frequency is 340 MHz.
−34 0 20 40 60 80 100 120 140 160
−33
−32
−31
−30
−29
−28
−27
−26
−25
Frequency in MHz
Magnitude in dB
Figure 5.13: Transfer function mismatch with 1% gain mismatch, -1% time-skew
mismatch and 2% bandwidth mismatch. The sampling frequency is 340 MHz.


```
Signal generator Lowpass filter Postprocessingon PC
```
```
Zynq SoC FPGA
```
```
AD- FMCOMMS1-EBZ
```
```
Figure 5.14: Test bench
```
```
Figure 5.15: Xilinx Zynq 7000 All Programmable SoC zc702 Evaluation Kit
```
### 5.6 Measurement results on two-channel ADC board

Our technique was tested on a 14-bits two-channel ADCs AD9643 from Analog
Devices. Fig. 5.14 shows the testbench used. The AD-FMCOMMS1-EBZ is
an analog front end hardware platform that contains the two-channel ADCs
AD9643 and it is connected to the Xilinx Zynq 7000 All Programmable SoC
zc702 Evaluation Kit FPGA Platform. The output samples are collected on a
computer where the spectrum is displayed. The FPGA platform Xilinx Zynq
7000 All Programmable SoC zc702 Evaluation Kit is shown on Fig. **??** and the
AD-FMCOMMS1-EBZ is shown on Fig. 5.16 and 5.17.


```
Figure 5.16: AD-FMCOMMS1-EBZ
```
The input signal consists of a sinusoid of amplitude 0_._ 35 V at frequency
_f_ 0 = 31MHz. The estimation uses the adaptive filtering structure of Fig. 5.3
and the compensation uses the structure of Fig. 5.6.

Fig. 5.18(a) shows the output spectrum before calibration with a sampling
frequency _fs_ = 140MHz. Gain, time-skew and bandwidth mismatch errors cre-
ate a spurious which occurs at frequency _fspur_ =− _f_ 0 + _f_ 2 _s_ = 39MHz and its
magnitude is− 64 dB. Offset mismatch creates a spurious of magnitude− 64 dB
at the DC component and a spurious of magnitude− 57 dB at the nyquist fre-
quency. The other spurious visible on the spectrum are inherent to the individ-
ual sub-ADCs we have used and are not due to interleaving.

A compensation of offset mismatch errors has been used in order to remove
the DC component and the spurious at the nyquist frequency. For this purpose
we have subtracted the mean amplitude from each sample. Fig. 5.18(b) shows
the output spectrum after calibration with 51 taps compensation FIRs. The
digital calibration method we propose is able to reduce the magnitude of the
spurious due to gain, time-skew and bandwidth mismatches to− 102 dB i.e an
improvement of 38 dB. Fig. 5.19 shows the speed of the algorithm for the esti-
mation of the gain, time-skew and bandwidth mismatches. We need practically
10-K samples for the estimation of the three mismatches which is faster than
[5] and approximately the same speed obtained in [18].

```
Fig. 5.20 shows that the correction of channel mismatch errors increases
```

Figure 5.17: AD9643 on the AD-FMCOMMS1-EBZ functional blocks
with the number of taps and the achievable limit is 38 dB obtained with 51 taps
FIRs. However the dynamic performances are limited by the presence of some
spurious which are due to the internal imperfections of the individual sub-ADCs
we have used for this work.

```
Frequency in MHz
```
```
Magnitude in dB 0 10 20 30 40 50 60 70
-200
```
```
-150
```
```
-100
```
```
-50
```
```
0
Before Calibration
```
```
Frequency in MHz
Magnitude in dB^010203040506070
```
```
-200
```
```
-150
```
```
-100
```
```
-50
```
```
0
(a) After Calibration
```
```
(b)
```
Figure 5.18: Measurement results of the output spectrum before and after cali-
bration


```
Number of K-Samples
```
```
0 5 10 15 20 25
```
```
Estimated mismatches in %
-0.1
```
```
0
```
```
0.1
```
```
0.2
```
```
0.3
```
```
0.4
```
```
0.5
```
```
0.6
```
```
0.7
```
```
0.8
```
```
Convergence of estimation
```
```
Gain
Time-Skew
Bandwidth
```
Figure 5.19: Measurement results of the mismatch estimation convergence


```
20 30 40 50 60 70 80
```
```
10
```
```
15
```
```
20
```
```
25
```
```
30
```
```
35
```
```
40
```
```
Number of taps
```
```
Improvement in dB
```
Figure 5.20: Reduction of spurious magnitude with the number of taps of cor-
rection filters

### 5.7 ASIC synthesis

The algorithm we presented in the previous section was described with a high
level description tool such as Matlab/Simulink. In addition some simulations
and measurements were carried out to verify the correctness of the algorithm.
Now we are going to evaluate the area and the power consumption in the 65 nm
CMOS process.

Fig. 5.21 shows the flow diagram of the ASIC synthesis. If the calibration
algorithm presented above is designed in floating point data type, it will finally
be implemented in a fixed-point architecture. In the previous section, when
considering all mismatches for a two-channel TI-ADCs, the highest linearity
was obtained with two 51 taps FIR filters as shown on Fig. 5.20 and Fig. 5.6.
Therefore, for the ASIC synthesis we are going to consider two 51 taps FIR
filters. However a lower number of taps can be chosen if less linearity is desired.
In order to find the optimal word length data, we compute the SNDR of the
compensated signal in function of the word length as shown on Fig. 5.22. From
this analysis, we can see that the highest SNDR is 82 dB and is obtained with
15 bits. As a consequence, we will consider a word length of 15 bits. If less
linearity is desired, a lower value can be chosen.

After that, the behavioral algorithm should be described in a Hardware
Description Language such as Verilog for our case. Then some cosimulations
must be done to verify that the algorithm works well in this HDL language.
The last step consist in doing the logic synthesis in a process technology. In the
65 nm process, a power consumption of 10 mW and an area of 0_._ 035 mm^2 were
found.


Behavioral algorithm
in floating point

```
Verification
```
Behavioral algorithm
in fixed-point

```
HDL Description
```
Gate level synthesis

```
Verification
```
```
Verification
```
```
Figure 5.21: ASIC synthesis flow
```

```
Wordlength in bits
```
```
5 10 15 20 25 30 35
```
SNDR in dB

```
0
```
```
10
```
```
20
```
```
30
```
```
40
```
```
50
```
```
60
```
```
70
```
```
80
```
```
90
```
```
Before calibration
After calibration
```
```
Figure 5.22: SNDR in function of the word length
```

### 5.8 Conclusion

In this chapter, we have proposed a fully digital calibration technique of gain,
time-skew and bandwidth mismatches in TI-ADCs. The calibration is divided
into two independent steps: estimation and compensation. The estimation uses
a rational fractional delay filter combined to a lowpass filter to estimate adap-
tively the different mismatches. It is done blindly so that the ADC keeps running
while estimation is being processed. The compensation is based on the devel-
opment of a matrix approach to cancel the effects of channel mismatch errors.
This technique can be applied to any interleaved factor with a high flexibility.

Measurements were carried out on a two-channel ADC board AD9643 from
Analog Devices and results show the with only 10-K samples, gain, time-skew
and bandwidth mismatches can be estimated. The linearity can be improved
by almost 40 dB. With this algorithm we can expect a power consumption of
10 mW and a chip area of 0_._ 035 mm^2 for two 51 taps FIR filters and with 15
bits.


## Chapter 6

# Conclusion and

# Perspectives

In this work we designed a digital blind calibration algorithm which corrects
all channel mismatches in Time-Interleaved ADCs. First a considerable model-
ing effort of a single ADC was made to derive the differential equations of the
circuit and to find the analog variables responsible for distortion. For exam-
ple in chapter 2, the gain, time-skew, bandwidth and offset of a single ADC
were studied. We also made a deterministic and statistical analysis of harmonic
distortion in differential bootstrapped S/H circuits. We saw that mismatches
between the p-channel and n-channel must be lower than 1 % to have substantial
second harmonic distortion in the order of 100 dB. In chapter 3, this model of
a single ADC was completed with the statistical description of noises in term of
probability density function and power spectral density.

Then later in chapter 4, this model of a single ADC was used to derive closed
form equations for TI-ADCs. A general deterministic mismatch model including
the bandwidth was provided. The transfer function mismatch of a given chan-
nel was defined and related to its gain, time-skew and bandwidth mismatches.
In addition to this deterministic model, when considering random character of
manufacturing process, the resulting mismatches and spurious become also ran-
dom variables and their description involves necessarily a statistical modeling.
That’s why we also provided a statistical description of the SFDR in term of
probability density function and the probability to be lower than a critical value.
Therefore, for a level of performance determined by a minimum SFDR and its
probability of achievement we can specify the required mismatch dispersion.
This practical information becomes of relevant importance to establish robust
design with safe margins.

Based on the TI-ADC model developed in chapter 4, a fully digital calibra-
tion algorithm was derived. The calibration consisted into mismatch estimation
and compensation. The estimation used a rational fractional delay filter com-
bined to a lowpass filter to estimate adaptively the different mismatches. The
estimation was done blindly so that the ADC can keep running while estima-
tion is being processed. Numerical results show that all the mismatches can


be estimated with less than 10-K samples which is fast compared to the state
of art. In addition, the accuracy of the mismatch estimation is 98%, 94% and
88% for gain, time-skew and bandwidth mismatches. The compensation was
based on the development of a matrix approach to cancel the effects of chan-
nel mismatch errors. The method was tested with a two-channel ADC board
from Analog Devices and the results show that the linearity can be improved
by almost 40 dB. The ASIC synthesis of the calibration algorithm in 65 nm
GPLVT process shows that we can expect a power consumption in the order of
10 mW and an area consumption in the order of 0_._ 035 mm^2 with two 51 taps
compensation filters and with signals on 15 bits.

The calibration algorithm we developed assumes that the on-resistance is
constant i.e independent of the input signal. However as we saw in chapter 2,
this is not the case and the distortion created can be reduced by modifying the
analog front end of the ADC with a bootstrapped circuit. As an perspective we
can foresee a fully digital calibration which remove the nonlinearity created by
the signal dependency of the on-resistance of the S/H and which also corrects
channel mismatch errors. We can also apply the same method than that of used
for the nonlinearity of the bootstrap to analyze other errors like charge injection
and clock feedthrough.


## Bibliography

```
[1]Boris Murmann. Adc performance survey 1997-2014 available at
http://www.stanford.edu/ murmann/adcsurvey.html.
```
```
[2]Kurosawa Naoki, Kobayashi Haruo, Maruyama Kaoru, Hidetake Sugawara,
and Kensuke Kobayashi. Explicit analysis of channel mismatch effects in
time-interleaved adc systems. IEEE Transactions on Circuits and Systems ,
48:261–271, 2001.
```
```
[3]Stéphane Paquelet, Gaël Kamdem De Teyou, and Yann Le Guillou. Ti-adcs
sfdr requirement analysis. IEEE International New Circuits and Systems
Conference , 2013.
```
```
[4]Shafiq M. Jamal et all. Calibration of sample-time error in a two-channel
time-interleaved analog-to-digital converter. IEEE Trans. on Circuits and
Syst I. , 51:130–139, 2004.
```
```
[5]P. Satarzadeh, B. C. Levy, and P. J. Hurst. Adaptive semiblind calibration
of bandwidth mismatch for two-channel time-interleaved adcs. IEEE Trans.
on Circuits and Syst. , 56:2075–2088, 2009.
```
```
[6]Steven Huang and Bernard C. Levy. Adaptive blind calibration of tim-
ing offset and gain mismatch for two-channel time-interleaved adcs. IEEE
Trans. on Circuits and Syst. , 53:1278–1288, 2006.
```
```
[7]David Camarero. Mixed-signal clock-skew calibration in time-interleaved
analog-to-digital converters. PhD thesis, Tlcom ParisTech, 46 rue barrault,
75013, Paris, France, 2007.
```
```
[8]Philippe Benabes, Caroline Lelandais-Perrault, and Nicolas Le Dortz. Mis-
match calibration methods for high-speed time-interleaved adcs. Proceed-
ings of the 12th IEEE International New Circuits and Systems Conference ,
2014.
```
```
[9]Gaël Kamdem De Teyou, Hervé Petit, and Patrick Loumeau. Adaptive and
digital blind calibration of transfer function mismatch in time-interleaved
adcs. IEEE International New Circuits and Systems Conference , 2015.
```
[10]Han Le Duc et al. A fully digital background calibration of timing skew
in undersampling ti-adc. _IEEE International New Circuits and Systems
Conference_ , 2014.


[11]F. Rivet, A. Mariano, D. Dallet, and J-B. Begueret. A mixed-signal built-in
self-calibrated time-interleaved adc in 65 nm cmos technology. _IEEE New
Conference on Circuits and Systems_ , 2010.

[12]N. Le Dortz et. al. A 1.6gs/s time-interleaved sar adc with fully digi-
tal background mismatch calibration achieving interleaving spurs below 70
dbfs. _IEEE Solid-State Circuits Conference_ , 2014.

[13]Jonas Elbornsson. _Analysis, Estimation and Compensation of Mismatch
Effects in A/D Converters_. PhD thesis, Department of Electrical Engi-
neering, University of Linkopings, Sweden, 2003.

[14]Dusan Stepanovic. _Calibration Techniques for Time-Interleaved SAR A/D
Converters_. PhD thesis, University of California Berkeley, USA, 2012.

[15]Vijay Divi and Gregory W. Wornell. Blind calibration of timing skew in
time-interleaved analog-to-digital converters. _IEEE Journal Of Selected
Topics In Signal Processing._ , 3:509–522, 2009.

[16]Raouf Khalil, Marie-Minerve Louerat, Roger Petigny, and Hugo Gicquel.
Background time skew calibration for time-interleaved adc using phase de-
tection method. _IEEE New Circuits and Systems Conference._ , 2012.

[17]Tsung-Heng Tsai, Paul J. Hurst, and Stephen H. Lewis. Bandwidth mis-
match and its correction in time-interleaved analog-to-digital converters.
_IEEE Trans. on Circuits and Syst II._ , 53:1133–1137, 2006.

[18]Fatima Ghanem. _Bandwidth Mismatch Calibration in Time-Interleaved
Analog-to-Digital Converters_. PhD thesis, Telecom ParisTech, France,
2012.

[19]Paul J. Hurst Tsung-Heng Tsai and Stephen H. Lewis. Correction of mis-
matches in a time-interleaved analog-to-digital converter in an adaptively
equalized digital communication receiver. _IEEE Trans. on Circuits and
Syst I._ , 56:307–319, 2009.

[20]Shahzad Saleem and Christian Vogel. Adaptive blind background calibra-
tion of polynomial-represented frequency response mismatches in a two-
channel time-interleaved adc. _IEEE Trans. on Circuits and Syst I._ , 58:1300–
1310, 2011.

[21]A. Bonnetat, J-M Hodé, D. Dallet, and G. Ferré. A new fully digital
frequency response mismatch compensation algorithm for time-interleaved
analog-to-digital converters. _IEEE International Radar Conference_ , 2014.

[22]Texas Instruments. Understanding data converters. Technical report, Texas
Instruments, 1995.

[23]Walt Kester. Understand sinad, enob, snr, thd, thd + n, and sfdr so you
don’t get lost in the noise floor. Technical report, Analog Device.

[24]Boris Murmann. Thermal noise in track-and-hold circuits, analysis and
simulation techniques. _IEEE Solid-State Circuits Magazine_ , pages 46–54,
2012.


[25]P. Hurst, S. Lewis, P. Gray, and R. Meyer. _Analysis and Design of Analog
Integrated Circuits_. New York: Wiley, 2001.

[26]Behzad Razavi. _Principles of Data Conversion System Design._ IEEE Press,
NY, 1995.

[27]A. M. Abo and P. R. Gray. A 1.5-v, 10-bit, 14.3-ms/s cmos pipeline analog-
to-digital converter. _IEEE Journal Of Solid-State Circuits_ , 34:599–606,
1999.

[28]H. Pan et al. A 3.3-v 12-b 50-ms/s a/d converter in 0.6 um cmos with over
80 db sfdr. _IEEE Journal Of Solid-State Circuits_ , 35:599–606, 2000.

[29]S. Gupta, M. Choi, M. Inerfield, and J. Wang. A 1 gs/s 11b time-interleaved
adc in 0.13 um cmos. _IEEE International Of Solid-State Circuits Confer-
ence_ , 2006.

[30]P. R. Gray et al. _Analysis and Design and Analog Integrated Circuits_. New
York Wiley, 2001.

[31]P. Satarzadeh, B. C. Levy, and P. J. Hurst. Digital calibration of a nonlinear
s/h. _IEEE Journal Of Selected Topics In Signal Processing_ , 3:454–471,
2009.

[32]Liang Dai and Ramesh Harjani. Cmos switched-op-amp-based sample-and-
hold circuit. _IEEE Journal Of Solid-State Circuits_ , 35:109–113, 2000.

[33]M. Waltari. _Circuit Techniques for Low-Voltage and High-Speed A/D Con-
verters_. PhD thesis, Helsinki University of Technology, 2002.

[34]H.K. Data converters, 2005.

[35]M. WALTARI and K. HALONEN. A 220-msample/s cmos sample-and-
hold circuit using double-sampling. _Analog Integrated Circuits and Signal
Processing_ , 18:21–31, 1999.

[36]M. WALTARI and K. HALONEN. Timing skew insensitive switching for
double-sampled circuits. _Proceedings of the 1999 IEEE International Sym-
posium on Circuits and Systems_ , 2:61–64, 1999.

[37]Anand Mohan. _A Reconfigurable High Speed Analog to Digital Converter
Architecture for Ultra Wideband Devices_. PhD thesis, Faculty of Health,
Engineering and Science of Victoria University, Australia, 2010.

[38]Y. Creten, P. Merken, W. Sansen, R.P. Mertens, , and C. Van Hoof. An 8-
bit flash analog-to-digital converter in standard cmos technology functional
from 4.2 k to 300 k. _IEEE Journal of Solid-State Circuits_ , 44:2019–2025,
2009.

[39]M.O. Shaker & S. Gosh & M.A. Bayoumi. A 1-gs/s 6-bit flash adc in 90 nm
cmos. _IEEE International Midwest Symposium on Circuits and Systems,
MWSCAS_ , pages 144–147, 2009.

[40]Walt Kester. Adc architectures ii: Successive approximation adcs
available at [http://www.analog.com/static/imported-files/tutorials/mt-](http://www.analog.com/static/imported-files/tutorials/mt-)
021.pdf. Technical report, Analog Device, 2008.


[41]Xuan-Lun Huang, Ping-Ying Kang, Hsiu-Ming Chang, and Jiun-Lang
Huang. A self-testing and calibration method for embedded successive
approximation register adc. _IEEE Design Automation Conference (ASP-
DAC), Asia and South Pacific_ , pages 713–718, 2011.

[42]M. Casubolo & M. Grassi & A. Lombardi & F. Maloberti & P. Malcovati.
A two-bit-percycle successive-approximation adc with background offset
calibration. _IEEE International Conference on Electronics, Circuits and
Systems_ , pages 650–653, 2008.

[43]Bonnie Bakerr. How delta-sigma adcs work, part 1 available at
[http://www.ti.com/lit/an/slyt423/slyt423.pdf.](http://www.ti.com/lit/an/slyt423/slyt423.pdf.) Technical report, Texas In-
struments Incorporated, 2011.

[44]Erkan Alpman. _A 7 bit 2.5 GS/sec Time-Interleaved C-2C SAR ADC for
60 GHz Multi-Band OFDM-Based Receivers_. PhD thesis, Department of
Electrical and Computer Engineering, Carnegie Mellon University, 2009.

[45]Tibi Galambos. Adc performance metrics, measurement and calibration
techniques. Technical report, PMC-s=SIERRA, 2009.

[46]A. B. Sripad and D. L. Snyder. A necessary and a sufficient condition
for quantization errors to be uniform and white. _IEEE Transactions On
Acoustics, Speech and Signal Processing._ , 25:442–448, 1977.

[47]Russell K. Hobbie and Bradley John Roth. _Intermediate physics for
medicine and biology_. Springer, 2007.

[48]X. Gao, E. A. M. Klumperink, P. F. J. Geraedts, and B. Nauta. Jitter
analysis and a benchmarking figure-of-merit for phase-locked loops. _IEEE
Transactions On Circuits ans systems II._ , 56:117–121, 2009.

[49]Thomas Neu. Clock jitter analyzed in the time domain part 1 available
at [http://www.ti.com/lit/an/slyt379/slyt379.pdf.](http://www.ti.com/lit/an/slyt379/slyt379.pdf.) Technical report, Texas
Instrument Incorporated, 2010.

[50]Andrew Fogg. Baseband / rf digital interface specification. logi-
cal, electrical and timing characteristics, egprs version available at
[http://mid.mipi.org/docs/digrf_standard_v112.pdf.](http://mid.mipi.org/docs/digrf_standard_v112.pdf.) Technical report,
Digital Interface Working Group, 2004.

[51]M. Lohning and G. Fettweis. The effects of aperture jitter and clock jitter
in wideband adcs. _Computer Standards and Interfaces_ , 2007.

[52]Ali Hajimiri, Sotirios Limotyrakis, and Thomas H. Lee. Jitter and phase
noise in ring oscillators. _IEEE Journal of Solid-State Circuits_ , 34:790–804,
1999.

[53]B. Razavi. Noise, lecture, fall 11 ee university of california la available at
[http://www.ee.ucla.edu/](http://www.ee.ucla.edu/) brweb/teaching/215a_f2011/noise.pdf.

[54]Yann Le Guillou. _Contribution l’tude de la conversion analogique-numrique
sigma-delta intgre dans une chaine de rception radiofrquence pour les ap-
plications cellulaires_. PhD thesis, University of Caen, France, 2005.


[55]Jennifer Eve Hoffman. _A Search for Alternative Electronic Order in the
High Temperature Superconductor Bi2Sr_ 2 _CaCu_ 2 _O_ 8+? _by Scanning Tun-
neling Microscopy_. PhD thesis, University of California Berkeley, USA,
2003.

[56]M. E. Chammas and B. Murmann. General analysis on the impact of
phase-skew in time-interleaved adcs. _IEEE Trans. on Circuits and Syst. I:
Regular Papers_ , 56:902–910, 2004.

[57]Gildas Leger et. al. Impact of random channel mismatch on the snr and sfdr
of time-interleaved adcs. _IEEE Trans. on Circuits and Syst._ , 51:140–150,
2009.

[58]Christian Vogel. The impact of combined channel mismatch effects in
time-interleaved adcs. _IEEE Trans. on Instrumentation and Measurement_ ,
54:415–427, 2005.

[59]K. Poulton et all. A 20 gs 8b adc with a 1 mb memory in 0.18um cmos. _Pro-
ceedings of IEEE International Solid-State Circuits Conference._ , 55:318–
496, 2003.

[60]B. Nauta X. Gao and E. Klumperink. Advantages of shift registers over
dlls for flexible low jitter multiphase clock generation. _IEEE Transactions
On Circuits and Systems II: Express Briefs._ , 55:244–248, 2008.

[61]H. Mahmoodi, S. Mukhopadhyay, and K. Roy. Estimation of delay varia-
tions due to random-dopant fluctuations in nanoscale cmos circuits. _IEEE
Journal of Solid-State Circuits_ , 40:1787–1796, 2005.

[62]S. M. Louwsma, A. J. M van Tuijl, M. Vertregt, and B. Nauta. A 1.35
gs/s, 10 b, 175 mw time-interleaved ad converter in 0.13 _μ_ m cmos. _IEEE
Journal of Solid-State Circuits_ , pages 778–786, 2008.

[63]Gaël Kamdem De Teyou, Hervé Petit, Patrick Loumeau, Hussein Fakhoury,
Yann Le Guillou, and Stéphane Paquelet. Statistical analysis of noise in
broadband and high resolution adcs. _IEEE International Conference on
Circuits and Systems_ , 2014.

[64]Javier Diaz-Carmona* Gordana Jovanovic-Dolecek. One method for fir
fractional delay filter design. _Proceedings of the Fourth IEEE International
Caracas Conference on Devices Circuits and Systems_ , 2002.

[65]Y. Chiu. Sample and hold basics. University Lecture, 2012.

[66]Parastoo Nikaeen. _Digital Compensation Of Dynamic Acquisition Errors
At The Front-End Of ADCs_. PhD thesis, University of Stanford, USA,
2008.

[67]M. Al-Shyoukh, D. Aksin, and F. Maloberti. Switch bootstrapping for pre-
cise sampling beyond supply voltage. _IEEE Journal of Solid-State Circuits_ ,
41:1938–1943, 2006.

[68]M. Al-Shyoukh, D. Aksin, and F. Maloberti. Switch bootstrapping for pre-
cise sampling beyond supply voltage. _IEEE Journal Of Solid-State Circuits_ ,
2006.


[69]D. Bormann et al. A multiband multistandard notch filter lna for lte,
wcdma and gsm for saw-less frontends. _Proceedings of the Asia-Pacific
Microwave Conference_ , pages 498–501.

[70]T. ltakura. Effects of the sampling pulse width on the frequency charac-
teristics of a sample-and-hold circuit. _IEEE Procedings, Circuits, Devices
and Systems_ , 141:328–336, 1994.

[71]Bob Verbruggen, Masao Iriguchi, and Jan Craninckx. A 1.7mw 11b 250mss
2x interleaved fully dynamic pipelined sar adc in 40nm digital cmos. _IEEE
International Solid-State Circuits Conference_ , 2012.

[72]Jonas Elbornsson. _Analysis, Estimation and Compensation of Mismatch
Effects in AD Converters_. PhD thesis, Linkpings universitet, SE 581 83
Linkping, Sweden, 2003.

[73]Paul Horowitz and Hill Winfield. _The Art of Electronics_. Cambridge Uni-
versity Press, 1989.

[74]Leo P. Mulcahy. Statistical an alysis of digital fixed-point multiplication
errors and quantization errors. _National Technical Information Service_ ,
pages 7–8, 1971.

[75]Brian Black. Analog-to-digital converter architectures and choices for sys-
tem design. _Analog Dialogue_ , 33-8, 1999.

[76]Inc Analog Device. _Linear Circuit Design Handbook_. Hank Zumbahlen,
2008.

[77]Gupta Sachin and Phatak Akshay. Adc guide, part 3: Offset errors. Tech-
nical report, Cypress Semiconductor Corp.

[78]E. B. Loewenstein. _The Measurement, Instrumentation and Sensors Hand-
book on CD-ROM_. Crc Press Llc, 1999.

[79]KOBAYASHI Haruo, MOFUMURA Masanao, KOBAYASHI Kensuke, and
ONAYA Yoshitaka. Aperture jitter effects in wideband adc systems.
_IEEE/SICE International Symposium on System Integration_ , 1999.

[80]Michael Lohning and Gerhard Fettweis. The effects of aperture jitter and
clock jitter in wideband adcs. _Computer Standards and Interfacese_ , 29:11–
18, 2007.

[81]Walt Kester. Aperture time, aperture jitter, aperture delay time— remov-
ing the confusion. Technical report, Analog Devices, 2009.

[82]Mike Tyler. _he Mechatronics Handbook - 2 Volume Set_. Robert H. Bishop
CRC Press 2002, 2002.

[83]Christopher Taillefer. _Analog-to-Digital Conversion via Time-Mode Signal
Processing_. PhD thesis, McGill University, Montral, 2007.

[84]MAXIM IC. Adc and dac glossary, Jul 2002.


[85]ANEKAL B. SRIPAD and DONALD L. SNYDER. A necessary and suf-
ficient condition for quantization errors to be uniform and white. _IEEE
TRANSACTIONS ON ACOUSTICS, SPEECH, AND SIGNAL PRO-
CESSING_ , 5:443–448, 1977.

[86]Walt Kester. Understand sinad, enob, snr, thd, thd + n, and sfdr so you
don’t get lost in the noise floor. Technical report, Analog Devices, 2008.

[87]Claude Shannon. Communication in the presence of noise. _Institute of
Radio Engineers_ , 37:10–21, 1949.

[88]Haruo Kobayashi, Kensuke Kobayashi, Masanao Morimura, Yoshitaka On-
aya, Yuuich Takahashi, Kouhei Enomoto, and Hideyuki Kogure. The effects
of aperture jitter and clock jitter in wideband adcs. _IEICE Transactions
Fundamentals_ , 85:335, 2002.

[89]E.J. Peralias, A. Rueda, J.L. Huertas, and G. Leger. Impact of random
channel mismatch on the snr and sfdr of time-interleaved adcs. _IEEE
Transactions on Circuits and Systems_ , 51:140–150, 2004.

[90]C. Jun, R. Feng, and X. Mei-hua. Ic design of 2ms/s 10-bit sar adc with
low power. _International Symposium on High Density packaging and Mi-
crosystem Integration_ , pages 1–3, 2007.



## List of Figures

```
1 Architecture d’un récepteur superheterodyne conventionnel.... 8
2 Radio logicielle idéale......................... 8
3 Stand alone ADCs performance survey from 1997 to 2015..... 9
4 Time Interleaved ADCs architecture................. 10
5 Simulation results of the on-resistance of a bootstrapped S/H as a
function of the input signal in 65 nm CMOS process with supply
voltage of vdd = 1. 2 V......................... 12
6 Logical structure of the bootstrap circuit.............. 12
7 PDF of a two-channel TI-ADCs with a gain mismatch of 1 % and
with a input sinusoid of amplitude 1 V............... 15
8 PDF of a two-channel TI-ADCs with a time-skew mismatch of
1 %, a sampling frequency of 320 MHz and with a input sinusoid
of amplitude 1 V and a frequency of 137 MHz........... 15
9 PDF of a two-channel TI-ADCs with a bandwidth mismatch of
1 %, a sampling frequency of 320 MHz and with a input sinusoid
of amplitude 1 V, a frequency of 137 MHz and a cutoff frequency
of 160 MHz.............................. 16
10 Adaptive filtering structure..................... 17
11 Simulation of the Convergence of mismatch estimation...... 18
12 SFDR before and after correction with a two-channel TI-ADCs
with 1% gain mismatch, -1% time-skew mismatch and 2% band-
width mismatch. The sampling frequency is 340 MHz....... 19
13 Test bench used for the measurements............... 19
14 Reduction of spurious magnitude with the number of taps of cor-
rection filters............................. 20
15 Measurement results of the output spectrum before and after
calibration............................... 20
```
```
1.1 Conventional superheterodyne architecture............. 23
1.2 The ideal software defined radio architecture............ 23
1.3 Stand alone ADCs performance survey from 1999 to 2014..... 24
1.4 Time Interleaved ADCs architecture................. 25
```
```
2.1 Static characteristic of an ADC with offset............. 31
2.2 Static characteristic of an ADC with gain error.......... 32
2.3 Static characteristic of an ADC with nonlinearities........ 33
2.4 Open-loop S/H diagram (a) and its equivalent first order model
(b).................................... 35
2.5 Clock distribution circuit of a single ADC.............. 36
```

2.6 Logical structure of the bootstrap circuit.............. 37
2.7 Simulations result of the on-resistance of a bootstrapped S/H as a
function of the input signal in 65 nm CMOS process with supply
voltage of _vdd_ = 1_._ 2 V......................... 38
2.8 Statistical distribution of the slope a in 65 nm CMOS process
with supply voltage of _vdd_ = 1_._ 2 V.................. 38
2.9 Statistical distribution of the constant resistance _bon_ in 65 nm
CMOS process with supply voltage of _vdd_ = 1_._ 2 V......... 39
2.10 Correlation between _a_ and _b_ in 65 nm CMOS process with supply
voltage of _vdd_ = 1_._ 2 V......................... 40
2.11 Output spectrum of a S/H with _τ_ ( _x_ ) = (1_._ 25 _e_ −10 + 2_._ 3 _e_ − 11 _x_.
The input signal is _x_ ( _t_ ) = 0_._ 6 sin(2 _πfot_ ), _fo_ = 20MHz, _fs_ =
300 MHz and the number of fft points is 16384.......... 41
2.12 Differential Bootstrap S/H circuit.................. 42
2.13 Statistical distribution of second harmonic distortion of a differ-
ential bootstrapped S/H in 65 nm CMOS process with an input
signal _x_ ( _t_ ) = 0_._ 6 sin(2 _πfot_ ), _fo_ = 20MHz, _fs_ = 300MHz, a rela-
tive mismatch of 1.2 % and N = 50 points............. 44
2.14 Harmonic distortion law....................... 45
2.15 Charge injection and clock feedthrough............... 46
2.16 Typical close loop S/H circuit.................... 47
2.17 Switch Capacitor S/H circuit.................... 48
2.18 Double sampling technique..................... 48
2.19 Quantization characteristic..................... 49
2.20 A 2 bits Flash converter........................ 51
2.21 Successive Approximation Register.................. 53
2.22 Pipeline Converter Architecture................... 54
2.23 Delta Sigma ADC........................... 55
2.24 Mathematical model of a single ADC................ 55

3.1 (a): Typical S/H circuit. (b): Thermal noise source in a basic S/H. 60
3.2 Power spectral density of thermal noise.............. 61
3.3 Sampling frequency and ENOB due to thermal noise vs Hold
capacitor. Simulation done with _Non_ = 7, _Ron_ = 15and _A_ =
0_._ 75 _V pp_................................ 62
3.4 ENOB due to jitter vs input frequency............... 63
3.5 Aperture jitter in S/H circuit.................... 64
3.6 Power spectral density of aperture jitter noise in S/H with _fo_ =
80 MHz, _σapt_ = 0_._ 13 ps rms, _fs_ = 307_._ 2 MHz and _A_ = 0_._ 75 V _p_.. 65
3.7 Power spectral density of noise resulting from sampling a sinu-
soidal signal _x_ ( _t_ ) = 0_._ 6 sin(2 _πf_ 0 _t_ )with a clock generated by a
free-running oscillator. _fo_ = 75MHz, _σclk_ = 82 fs, _fs_ = 300MHz 67
3.8 Power spectral density of flicker, thermal and shot noise..... 68

4.1 M Time-Interleaved ADCs...................... 71
4.2 Clock diagram of the sub-ADCs................... 72
4.3 Sub-ADCs clock created by a phase generator........... 73
4.4 Shift Registers Phase generator for 4 sub-ADCs.......... 73
4.5 Clock distribution with inverters.................. 74


4.6 Output spectrum of a 4 TI-ADCs with bandwidth mismatch for
an input signal _x_ ( _t_ ) = 1_._ 5 sin(2 _πfot_ ), _fo_ = 146_._ 29 MHz and
_fs_ = 320MHz. [ _fcofc_ 1 _fc_ 2 _fc_ 3 ] = [4.07 3.80 3.98 3.85] GHz.... 77
4.7 Two chains of 13 inverters clocked at 50 MHz in 65 nm process.. 78
4.8 Time-skew mismatch between two channel of 13 inverters in 65 nm
process at a frequency of 50 MHz.................. 79
4.9 Typical CMOS inverter....................... 79
4.10 PDF of a two-channel TI-ADCs with a gain mismatch of 1 % and
with a input sinusoid of amplitude 1 V............... 81
4.11 PDF of a two-channel TI-ADCs with a time-skew mismatch of
1 %, a sampling frequency of 320 MHz and with a input sinusoid
of amplitude 1 V and a frequency of 137 MHz........... 81
4.12 PDF of a two-channel TI-ADCs with a bandwidth mismatch of
1 %, a sampling frequency of 320 MHz and with a input sinusoid
of amplitude 1 V, a frequency of 137 MHz and a cutoff frequency
of 160 MHz.............................. 82
4.13 SFDR distortion law......................... 84

5.1 Time-Interleaved ADCs....................... 90
5.2 Spectrum of the _mth_ ADC output................. 91
5.3 Adaptive filtering structure..................... 92
5.4 Multirate fractional rational delay _m/M_.............. 92
5.5 Principle of the fully digital calibration............... 93
5.6 Compensation structure for M=2.................. 94
5.7 Simulation of the Convergence of mismatch estimation...... 97
5.8 Simulation of the output spectrum before and after calibration. 97
5.9 SFDR before and after correction with a two-channel TI-ADCs
with 1% gain mismatch. The sampling frequency is 340 MHz.. 98
5.10 SFDR before and after correction with a two-channel TI-ADCs
with -1% time-skew mismatch. The sampling frequency is 340 MHz.
99
5.11 SFDR before and after correction with a two-channel TI-ADCs
with 2% bandwidth mismatch. The sampling frequency is 340 MHz.
99
5.12 SFDR before and after correction with a two-channel TI-ADCs
with 1% gain mismatch, -1% time-skew mismatch and 2% band-
width mismatch. The sampling frequency is 340 MHz....... 100
5.13 Transfer function mismatch with 1% gain mismatch, -1% time-
skew mismatch and 2% bandwidth mismatch. The sampling fre-
quency is 340 MHz.......................... 100
5.14 Test bench.............................. 101
5.15 Zynq SoC board........................... 101
5.16 AD-FMCOMMS1-EBZ........................ 102
5.17 AD9643 on the AD-FMCOMMS1-EBZ functional blocks..... 103
5.18 Measurement results of the output spectrum before and after
calibration............................... 103
5.19 Measurement results of the mismatch estimation convergence.. 104
5.20 Reduction of spurious magnitude with the number of taps of cor-
rection filters............................. 105
5.21 ASIC synthesis flow......................... 106


5.22 SNDR in function of the word length................ 107

A.1 Logical structure of the bootstrap circuit.............. 127
A.2 Clock diagram of a bootstrapped S/H............... 128



## List of Tables

```
2.1 Simulation results of a S/H with τ ( x ) = (1. 25 e −10+2. 33 e − 11 x.
The input signal is x ( t ) = 0. 6 sin(2 πfot ), fo = 20MHz, fs =
300 MHz................................ 41
2.2 Simulation results of a differential bootstrapped S/H with β =
0. 125 ns. The input signal is x ( t ) = 0. 6 sin(2 πfot ), fo = 20MHz
and fs = 300MHz........................... 43
2.3 Parameter values used to model S/H non-idealities in 28 nm HPL
technology............................... 46
2.4 Comparisons of differents converters achitectures......... 50
```
```
4.1 Expression of Qa........................... 75
4.2 Simulation results of a 4 TI-ADC with bandwidth mismatch for
an input signal x ( t ) = 1. 5 sin(2 πfot ), fo = 146. 29 MHz and
fs = 320MHz. [ fcofc 1 fc 2 fc 3 ] = [4.01 3.94 4.12 3.86] GHz.... 77
4.3 Matching needed to reach the desired SFDR of 90 dB in 99. 9 %
of cases with a 4 TI-ADCs, an input signal x ( t ) = 1. 5 sin(2 πf 0 t ),
f 0 = 146. 29 MHz and fs = 320MHz................. 84
```
```
5.1 SFDR in dB for a 2-channel at 40 MHz and 80 MHz....... 96
```


## Appendix A

# Appendix A: CMOS

# Bootstrapped and Sample

# and Hold Circuit

## A.1 On-resistance in function of the input signal

## in a single ended CMOS Bootstrap circuit

Fig. A.1 shows a the logical structure of a CMOS bootstrapped S/H circuit.
Ideally the gate-to-source voltage _vgs_ is now independent of the the input signal.
But due to parasitic capacitances at node _N_ 1 , mobility degradation and back
gate effet, this is not the case. For example, let’s call _Cp_ the parasitic capacitance
at note _N_ 1. The voltage _vgs_ can be written as:

```
vgs =
```
##### C 3

```
C 3 + Cp
```
```
vdd −
```
```
Cp
C 3 + Cp
```
```
x (A.1)
```
In (A.1), the gate-to-source voltage still depends of the input signal through _Cp_.
By replacing this value of _vgs_ in the expression of the on-resistance we obtain:

```
Ron =
```
##### [

```
μCox
```
##### W

##### L

##### (

```
vgs − vth
```
##### )]− 1

```
≃ bon + aonx
```
##### (A.2)

In (A.2), the parasitic capacitance has been considered small compared to the
bootstrap capacitance _C_ 3. _aon_ and _bon_ are given by:

```
aon =
```
##### 1

```
μCoxWL
```
##### [

```
C 3
C 3 + Cpvdd − vth
```
##### ]

```
bon =
```
```
Cp
C 3 + Cp
μCoxWL
```
##### [

```
C 3
C 3 + Cpvdd − vth
```
##### ]

##### (A.3)


##### C

##### -

```
r r
```
```
r
r
```
```
r
r
```
```
r r r r
```
```
vdd
```
##### Φ Φ

##### Φ

##### Φ

##### Φ

##### M 1

##### N 1

##### C 3

```
c
x ( t )
```
```
y[n]
c
```
```
Figure A.1: Logical structure of the bootstrap circuit.
```
From this we see that, the on-resistance still depends of the the input signal,
but in a linear manner. We have not considered the back gate effect and mo-
bility degradation. However, this linear dependency remains when considering
these nonidealities as simulation results of a CMOS bootstrapped S/H in 65 nm
process show it on Fig. 2.7.

### A.2 Output signal of a single ended bootstrap S/H circuit

Fig. A.2, shows the clock diagram of a S/H.

#### A.2.1 Sampling mode

During the sampling mode, the transistor-switch is _ON_ and the input signal
charges or discharges the hold capacitor so that the voltage _y_ ( _t_ )across the
capacitor is practically proportional to the the input voltage _x_ ( _t_ ). This stage
goes from _nTs_ − _βTs_ to _nTs_. _n_ is the index of a given sample at S/H output
and _βTs_ is the acquisition time which is taken as a fraction of the sampling
period _Ts_. A typical value of _β_ is^12. In this stage, The circuit is governed by
an inhomogeneous linear Ordinary Differential Equation (ODE) of first order:

```
y ( t ) + τ ( x )
```
```
dy ( t )
dt
```
```
= x ( t ) (A.4)
```
We can write (A.4) as:

```
y ′( t ) + A ′( t ) y = x ( t ) A ′( t ) (A.5)
In (A.5), y ′( t )is the derivate of y and the derivate A ′( t )is given by:
```

```
Clock signal
```
```
Input signal x ( t )
```
```
S/H output y(t)
```
```
Ts
```
```
βTs
```
(^0) _Ts_
−
_βT
s_
2 _T
s_
−
_βT
s_
3 _T
s_
−
_βT
s
Ts_ 2 _T
s_
3 _T
s
y_ [0]
_y_ [1] _y_ [2] _y_ [3]
Hold
Sampling
Hold
Sampling
Hold
Sampling
Hold
Figure A.2: Clock diagram of a bootstrapped S/H
_A_ ′( _t_ ) =

##### 1

```
τ ( x )
```
```
=
```
##### 1

```
b + ax ( t )
```
```
≃
```
##### 1

```
b
```
##### [

##### 1 −

```
a
b
```
```
x ( t )
```
##### ]

##### (A.6)

In (A.6), the time constant _τ_ ( _x_ )has been replaced by its linear expression
of section 2.2.3:

#### A.2.2 Hold mode

During this hold mode, the switch is OFF and the input signal is disconnected
from the capacitor. The voltage accross the capacitor is stored as the sampled
value _y_ [ _n_ ]. The equation governing the circuit is: voltage accross the capacitor
is stored as the sampled value _y_ [ _n_ ]. The equation governing the circuit is:

```
y ( t ) = y [ n ] = y ( nTs )
nTs ≤ t ≤( n + 1) Ts − βTs
```
##### (A.7)

We are going to solve the inhomogeneous linear ODE of(A.5) with the varia-
tion of parameters method. First we will find the solutions of the homegenoeus
equation associated to (A.5) and then we will find a particular solution.

#### A.2.3 Homogeneous ODE

The homogeneous ODE associated to (A.5) is:

```
y ′( t ) + A ′( t ) y = 0 (A.8)
The general solution y 0 of the homogeneous equation (A.8) is:
```

```
y 0 ( t ) = C 0 e − A ( t ) (A.9)
```
With _C_ 0 a constant parameter.

### A.3 Solution of the inhomogeneous equation

The general solution _y_ ( _t_ )can be written as:

```
y ( t ) = C ( t ) e − A ( t ) (A.10)
```
_y_ must satisfy (A.5). So by derivating _y_ and inserting this derivate in (A.5), we
find that:

```
C ′( t ) = A ′( t ) x ( t ) eA ( t ) (A.11)
```
We obtain _C_ by integrating (A.11):

```
C ( t ) =
```
```
∫ t
```
```
nTs − βTs
```
```
A ′( θ ) x ( θ ) eA ( θ ) dθ + C 1 (A.12)
```
In (A.12), _C_ 1 is a constant parameter that will be determined with the
intitial conditions and _A_ ( _t_ )is given by:

```
A ( t ) =
```
##### 1

```
b
```
```
∫ t
```
```
nTs − βTs
```
##### [

##### 1 −

```
a
b
x ( u )
```
##### ]

```
du
```
##### =

```
t − nTs − βTs
b
```
##### −

```
a
b^2
```
```
∫ t
```
```
nTs − βTs
```
```
x ( u )
```
##### (A.13)

And using the fact that _ax_ ≪ _b_ , we have:

```
e − A ( t )≃ e −
```
```
t − nTsb − βTs [
1 +
```
```
a
b^2
```
```
∫ t
```
```
nTs − βTs
```
```
x ( u ) du
```
##### ]

##### (A.14)

```
Inserting (A.12) and (A.14) in (A.10), we have:
```

_y_ ( _t_ ) =

```
[∫ t
```
```
nTs − βTs
```
```
A ′( θ ) x ( θ ) eA ( θ )+ C 1
```
##### ]

```
e − A ( t )
```
##### ≃

```
[∫ t
```
```
nTs − βTs
```
##### 1

```
b
```
##### (

##### 1 −

```
a
b
```
```
x ( θ )
```
##### )

```
x ( θ ) e
```
```
θ − nTs − βTs
b
```
##### (

##### 1 −

```
b
a^2
```
```
∫ θ
```
```
nTs − βTs
```
```
x ( u ) du
```
##### )

```
dθ
```
##### ]

```
.e −
```
```
t − nTs − βTs
b
```
##### [

##### 1 +

```
a
b^2
```
```
∫ t
```
```
nTs − βTs
```
```
x ( v ) dv
```
##### ]

##### =

##### 1

```
b
```
```
∫ t
```
```
nTs − βTs
```
```
x ( θ ) e −
```
```
t − θ
b
︸ ︷︷ ︸
y 1 ( t )
```
##### −

```
a
b^2
```
```
∫ t
```
```
nTs − βTs
```
```
x^2 ( θ ) e −
```
```
t − θ
b
︸ ︷︷ ︸
y 2 ( t )
```
```
−
a
b^3
```
```
∫ t
```
```
nTs − βTs
```
```
∫ θ
```
```
nTs − βTs
```
```
x ( u ) x ( θ ) e −
```
```
t − nTs − βTs
b e −
θ − nTs − βTs
b dudθ
︸ ︷︷ ︸
y 3 ( t )
```
```
+
```
```
a
b^3
```
```
∫ t
```
```
nTs − βTs
```
```
∫ θ
```
```
nTs − βTs
```
```
x ( v ) x ( θ ) e −
```
```
t − nTs − βTs
b e −
θ − nTs − βTs
b dvdθ
︸ ︷︷ ︸
y 4 ( t )
```
```
+ C 1 e −
```
```
t − nTs − βTs
b
```
##### [

##### 1 +

```
a
b^3
```
```
∫ t
```
```
nTs − βTs
```
```
x ( u ) du
```
##### ]

##### ︸ ︷︷ ︸

```
y 5 ( t )
(A.15)
```
**Initial Conditions**

At _t_ = _nTs_ − _βTs_ , we have:

```
y ( nTs − βTs ) = y [ n −1] = C 1 (A.16)
```
**Expressions of** _y_ 1 **...** _y_ 5

We can find the different expressions of _yi_ [ _n_ ]as:

```
y 1 [ n ] =
```
##### 1

```
b
```
```
∫ nTs
```
```
nTs − βTs
```
```
x ( θ ) e −
```
```
nTs − θ
b dθ
```
```
= ( h ⋆ x )( nTs )− α ( h ⋆ x )( nTs − βTs )
≃( h ⋆ x )( nTs )
```
##### (A.17)

With _α_ = _e_ −

_βTs
b_ ≃ 0 because the sampling duration is several time bigger than
the time constant. Nevertheless _α_ can be taken into account if cases arises.

```
y 2 [ n ] =−
```
```
a
b
```
```
∫ nTs
```
```
nTs − βTs
```
```
x^2 ( θ ) e −
```
```
nTsb − θ
dθ
```
```
= ( h ⋆ x^2 )( nTs )− α ( h ⋆ x^2 )( nTs − βTs )
≃( h ⋆ x^2 )( nTs )
```
##### (A.18)

```
y 3 [ n ] + y 4 [ n ] =
```
```
a
b^3
```
```
∫ nTs
```
```
nTs − βTs
```
```
e −
```
```
nTs − θ
b
```
```
∫ nTs
```
```
θ
```
```
e −
```
```
θ − bv
dvdθ
```
##### ≃

```
a
b
```
##### (

```
h ⋆
```
##### [

```
x. ( h ⋆ x )
```
##### ])

```
( nTs )
```
##### (A.19)


And _y_ 5 is given by:

```
y 5 [ n ] = y [ n −1] α
```
##### [

##### 1 +

```
a
b^2
```
##### (

```
( u ⋆ x )( nTs )−( u ⋆ x )( nTs − βTs )
```
##### )]

##### ≃ 0

##### (A.20)

```
Finally we have:
```
```
y [ n ] = y 1 [ n ] + y 2 [ n ] + y 3 [ n ] + y 4 [ n ] + y 5 [ n ]
```
```
= ( h ⋆ x )( nTs )−
```
```
a
b
```
##### {

```
( h ⋆ x^2 )( nTs )−
```
##### (

```
h ⋆
```
##### [

```
x. ( h ⋆ x )
```
##### ])

```
( nTs )
```
##### } (A.21)

### A.4 Output of the S/H without nonlinearities

Considering that, the S/H is enough linear in (A.21), the output of the S/H can
be written as:

_y_ [ _n_ ] = ( _h ⋆ x_ )( _nTs_ ) (A.22)
If we consider also, the time-skew _t_ 0 , the gain _G_ , the transfer function of the
S/H can be written as:

```
H ( f ) =
```
##### G

```
1 + jffc
```
```
e − j^2 πft^0 (A.23)
```

## Appendix B

# Spectrum of the TI-ADCs

### B.1 Spectrum of the DC Component

The DTFT of the DC component at the TI-ADCs output is given:

```
YDC ( f ) =
```
##### ∑+∞

```
n =−∞
```
```
On [ M ]exp(− j 2 πf nTs )
```
##### =

##### M ∑− 1

```
m =0
```
```
Om exp(− j 2 πf mTs )
```
##### +∑∞

```
k =−∞
```
```
exp(− j 2 πf kM Ts )
```
##### (B.1)

```
Poisson theorem states that:
```
##### +∑∞

```
k =−∞
```
```
exp(− j 2 πkf M Ts ) =
fs
M
```
##### +∑∞

```
k =−∞
```
```
δ
```
##### (

```
f − k
fs
M
```
##### )

##### (B.2)

```
Using (B.2), YDC in (B.1) becomes:
```
##### YDC =

```
fs
M
```
##### ∑+∞

```
k =−∞
```
##### M ∑− 1

```
m =0
```
```
Om exp
```
##### (

```
− j 2 πk
```
```
fs
M
```
```
mTs
```
##### )

```
δ
```
##### (

```
f − k
```
```
fs
M
```
##### )

##### =

```
fs
M
```
##### ∑+∞

```
k =−∞
```
##### [ M ∑−^1

```
m =0
```
```
Omζ − mk
```
##### ]

```
δ
```
##### (

```
f − k
```
```
fs
M
```
##### )

##### =

```
fs
M
```
##### ∑+∞

```
k =−∞
```
##### [ M ∑−^1

```
m =0
```
##### (

```
1 + δOm
```
##### )

```
O 0 ζ − mk
```
##### ]

```
δ
```
##### (

```
f − k
```
```
fs
M
```
##### )

##### (B.3)

Finally by separating harmonic frequencies _kfs_ from non-harmonic frequen-
cies _kMfs_ we obtain:


```
YDC ( f )
fs
```
##### =

##### +∑∞

```
k =−∞
```
```
Regular part
︷ ︸︸ ︷
[
1 +
```
##### 1

##### M

##### M ∑− 1

```
m =0
```
```
δOm (. )
```
##### ]

```
O 0 δ ( f − kfs )
```
##### +

##### +∑∞

```
∞
```
##### 1

##### M

##### [ M − 1

##### ∑

```
m =0
```
```
ζ − mkδmO
```
##### ]

```
O 0 δ ( f − k
```
```
fs
M
```
##### )

##### ︸ ︷︷ ︸

```
Spurious part
```
##### (B.4)

### B.2 Spectrum of the AC component

The DTFT of the AC component at the TI-ADCs output is given by:

_YAC_ ( _f_ ) =

##### +∑∞

```
n =−∞
```
```
yn [ M ]exp(− j 2 πf nTs )
```
##### =

##### M ∑− 1

```
m =0
```
```
exp(− j 2 πf mTs )
```
##### ∑+∞

```
k =−∞
```
```
( hm⋆ x )( kM Ts + mTs ) exp(− j 2 πf kM Ts )
```
##### =

##### M ∑− 1

```
m =0
```
```
exp(− j 2 πf mTs )
```
```
fs
M
```
##### +∑∞

```
k =−∞
```
```
exp
```
##### (

```
j 2 π (. ) mTs
```
##### )

```
Hm (. ) X (. )
```
##### ∣

##### ∣

##### ∣

```
f − kfMs
```
##### =

```
fs
M
```
##### +∑∞

```
k =−∞
```
##### [ M ∑−^1

```
m =0
```
```
ζ − mkHm (. )
```
##### ]

##### X (. )

##### ∣

##### ∣

##### ∣

```
f − kfMs
```
##### =

```
fs
M
```
##### +∑∞

```
k =−∞
```
##### [ M ∑−^1

```
m =0
```
```
ζ − mk
```
##### (

```
1 + δHm (. )
```
##### )]

##### H 0 (. ) X (. )

##### ∣

##### ∣

##### ∣

```
f − kfMs
(B.5)
```
Finally by separating harmonic replicas at _kfs_ from non-harmonic replicas
at _kfMs_ we obtain:

```
YAC ( f )
fs
```
##### =

##### +∑∞

```
k ̸=0[ M ]
−∞
```
##### 1

##### M

##### [ M − 1

##### ∑

```
m =0
```
```
ζ − mkδHm (. )
```
##### ]

##### H 0 (. ) X (. )

##### ︸ ︷︷ ︸

```
Spurious part
```
##### ∣

##### ∣

##### ∣

##### ∣

```
f − kfMs
```
##### +

##### ∑+∞

```
k =−∞
```
```
Regular part
︷ ︸︸ ︷
[
1 +
```
##### 1

##### M

##### M ∑− 1

```
m =0
```
```
δHm (. )
```
##### ]

##### H 0 (. ) X (. )

##### ∣

##### ∣

##### ∣

##### ∣

```
f − kfs
```
##### (B.6)


## Appendix C

# Statistical Analysis of

# TI-ADCs

### C.1 Probability Density Function of Sa ( k )

We have:

```
Sa ( k ) =
```
##### ∣

##### ∣

##### ∣

##### M ∑− 1

```
m =1
```
```
ζ − mkξam
```
##### ∣

##### ∣

##### ∣

```
2
```
##### =

##### [ M ∑−^1

```
m =1
```
```
cos
```
##### (

```
2 πmk
M
```
##### )

```
ξam
```
##### ] 2

##### +

##### [ M ∑−^1

```
m =1
```
```
sin
```
##### (

```
2 πmk
M
```
##### )

```
ξam
```
##### ] 2

```
= Xk^2 + Yk^2
```
##### (C.1)

_Xk_ and _Yk_ are two gaussian random variables as they are the sum of independent
gaussian random variables. In addition we have:E[ _XkYk_ ] =E[ _Xk_ ]E[ _Yk_ ]. As a
consequence _Xk_ and _Yk_ are two gaussian independent variables. Their PDF are
given by:

```



```
```
Xk =
```
##### [∑

```
M − 1
m =1cos
```
```
( 2 πmk
M
```
##### )

```
ξma
```
##### ]

##### ∼ N

##### (

##### 0 ,

##### √∑

```
M − 1
m =1cos
2 (^2 πmk
M
```
##### ))

```
Yk =
```
##### [∑

```
M − 1
m =1sin
```
```
( 2 πmk
M
```
##### )

```
ξam
```
##### ]

##### ∼ N

##### (

##### 0 ,

##### √∑

```
M − 1
m =1sin
```
```
2 ( 2 πmk
M
```
##### )) (C.2)

```
After the calculation of their variances we can see that:


```
```

```
```
Xk, Yk ∼N
```
##### (

##### 0 ,M 2 − 1

##### )

```
k ̸= M 2
Xk ∼N(0 , M −1) k = M 2
Yk ∼N(0 , 0) k = M 2
```
##### (C.3)

We can make the following analysis:

- If _k_ ̸= _M_ 2 , _Sa_ ( _k_ )is the sum of two independent squared gaussian random
    variables. As a consequence its PDF is a Chi-square law with two degree
    freedom _χ_^22.


- If _k_ = _M_ 2 , _Sa_ ( _k_ )is the square of a gaussian random variable. As a conse-
    quence its PDF is a Chi-square with one degree freedom _χ_^21.

### C.2 PDF of Smax

Let’s consider the case where _M_ is odd. For _M_ is even, the methodology is the
same. The random variables _Sa_ ( _k_ )follows a Chi-square distribution _χ_^22 with two
degrees of freedom. The demonstration is shown in Appendix C. C.1. Therefore
all the random variable _Sa_ ( _k_ )have the same PDF which is:

```
f 0 ( s ) =
```
##### 1

##### M ′

```
e
```
```
− s
M ′ (C.4)
```
With _M_ ′= _M_ − 2. The Cumulative Density Function _F_ 0 of the random variables
_Sa_ ( _k_ )is given by:

```
F 0 ( s ) = 1− e −
```
```
s
M ′ s > 0 (C.5)
```
The proof of (C.5) is detailed in Appendix C. C.3. For _M_ odd there are( _M_ −1) _/_ 2
spurs from _k_ = 1to _k_ = ( _M_ −1) _/_ 2. The CDF _Fmax_ of _Smax_ is the product of the
CDF of the different _Sa_ ( _k_ ) _k_ =1 _..._ ( _M_ −1) _/_ 2 as the different _Sa_ ( _k_ )are independent

[57]. As a consequence, we have:

```
Fmax ( s ) = ( F 0 ( s ))
```
```
M − 1
```
(^2) = (1− _e_ − _Ms_ )
_M_ − 1
(^2) (C.6)
The PDF _fmax_ of _Smax_ is obtained by differentiating its PDF:
_fmax_ ( _s_ ) =

##### M − 1

##### 2 M

```
e −
Ms (
1 − e −
Ms ) M −^23
(C.7)
```
From (4.16) and (C.7), we can find the PDF of the SFDR by a change of
variables:

### C.3 Cumulative Density Function of Sa ( k )

The Cumulative Density Function (CDF) is obtained by integrating the PDF.
For _k_ ̸= _M_ 2 odd, the CDF _F_ 0 is given by:

```
F 0 ( s ) =
```
```
∫ s
f 0 ( s ′) ds ′
```
##### =

```
∫ s
1
M
```
```
e −
Ms
```
```
= 1− e −
Ms
```
##### (C.8)

The constant 1 in (C.8) by considering the fact that _s >_ 0 and _F_ 0 (0) = 0.


## Appendix D

# Appendix E: Thermal Noise

#### D.0.1 Total power

Let’s denote _h_ ( _t_ ) = _Ron_^1 _Ce_ −
_Rt
onC, t >_ 0 , the impulse response of the RC S/H
of Fig. 2.4. The noise source is filtered trough _h_ and the total noise power at
S/H output is obtaining by integrating output noise in all frequencies :

```
v^2 thermal =
```
##### ∫+∞

```
−∞
```
```
2 kBT Ron
```
##### ∣

##### ∣

##### ∣

##### 1

```
1 + j 2 πRonCf
```
##### ∣

##### ∣

##### ∣

```
2
df
```
##### =

```
kBT
C
```
##### (D.1)

#### D.0.2 Power spectral density of thermal noise

_Rin_ ( _τ_ ) = 2 _kBT Ronδ_ ( _τ_ )denotes the autocorrelation function of thermal noise
across _Ron_. The autocorrelation of thermal noise at the S/H output is :

```
Rth ( τ ) = Rin ( τ ) ⋆ h ( τ ) ⋆ h (− τ )
```
```
=
```
```
kBT
C
```
```
e −
```
```
| τ |
RonC
```
##### (D.2)

```
In discrete mode (D.2) becomes :
```
```
Rth [ n ] =
kBT
C
```
```
e −
```
```
| n | Ts
RonC (D.3)
```
With _Ts_ the sampling period. The PSD _Sthermal_ of thermal noise at S/H output
is obtained by taking the Discrete Time Fourier Transform (DTFT) of _Rth_ :

```
Sthermal ( f ) =
```
##### 1

```
fs
```
##### +∑∞

```
n =−∞
```
```
Rth [ n ] exp(− j 2 πf nTs )
```
##### =

##### 1

```
fs
```
##### +∑∞

```
n =−∞
```
```
kBT
C
```
```
exp
```
##### (

##### −

```
| n | Ts
RonC
```
##### )

```
exp(− j 2 πf nTs )
```
##### (D.4)

```
Using the serie [? ] :
```

##### +∑∞

```
n =−∞
```
```
exp(−| na |) exp(− jnb ) =
```
```
sinh( a )
cosh( a )−cos( b )
```
##### (D.5)

We deduce that :

```
Sthermal ( f ) =
```
##### 1

```
fs
```
```
kBT
C
```
```
1 −exp(− R^2 onTsC )
1 −2 exp(− RTonsC ) cos(2 πffs ) + exp(− R^2 onTsC )
```
```
≃
```
##### 1

```
fs
```
```
kBT
C
```
##### (D.6)

The above approximation is valid because for ADCs of concern _Ron_ ∼10Ω,
_C_ ∼ 10 pF and _fs_ ∼ 300 MHz→exp(− _RTonsC_ )≪ 1.


## Appendix E

# Power Spectral Density of

# Jitter

### E.1 Useful property of WSS signal

##### E

##### [

```
X ( f 1 ) X ( f 2 )
```
##### ]

```
= δ ( f 2 − f 1 )E
```
##### [

```
| X ( f 2 )|^2
```
##### ]

##### (E.1)

This property comes from the fact that the autocorrelation function of a signal
can be written as :

```
Rxx ( τ ) =E
```
##### [∫+∞

```
−∞
```
```
X ( f 1 ) exp(− j 2 πf 1 t )
∫+∞
```
```
−∞
```
```
X ( f 2 ) exp
```
##### (

```
j 2 πf 2 ( t + τ )
```
##### )

```
d f 1 d f 2
```
##### ]

##### =

##### ∫+∞

```
−∞
```
##### ∫+∞

```
−∞
```
##### E

##### [

```
X ( f 1 ) X ( f 2 )
```
##### ]

```
exp
```
##### (

```
j 2 π ( f 2 − f 1 ) t
```
##### )

```
exp( j 2 πf 2 τ ) d f 1 d f 2
```
If the signal is stationnary, its autocorrelation function only doesn’t depend of
_t_.

### E.2 Autocorrelation function of jitter noise

Before evaluating the PSD of jitter noise, we should first evaluate the autocor-
relation of jitter noise. We find that, it is given by :

```
Ree ( k ) =E
```
##### {

```
e [ n ] e [ n + k ]
```
##### }

##### =E

##### [∫

```
f 1
```
```
X ( f 1 ) e − j^2 πf^1 nTs
```
##### (

```
e − j^2 πf^1 ε [ n ]− e − j^2 πf^1 ε [0]
```
##### )

##### ∫

```
f 2
```
```
X ( f 2 ) ej^2 πf^2 nTsej^2 πf^2 kTs
```
##### (

```
ej^2 πf^1 ε [ n + k ]− e − j^2 πf^1 ε [0]
```
##### )

```
d f 1 d f 2
```
##### ]

##### =

##### ∫

```
f 1
```
```
Sxx ( f 1 ) exp( j 2 πf 1 kTs )
{
1 +E
```
##### [

```
ej^2 πf^1 ( ξ [ n + k ]− ξ [ n ])
```
##### ]

##### −E

##### [

```
ej^2 πf^1 ξ [ n + k ]
```
##### ]

##### −E

##### [

```
ej^2 πf^1 ξ [ n ]
```
##### ]}

```
d f 1
```

### E.3 PSD of aperture jitter

As the aperture jitter is a gaussian white process, we have the following prop-
erties :

- E

##### [

```
ej^2 πf^1 ξ [ n ]
```
##### ]

```
= e −^2 π
```
(^2) _f_ 12 _σ_ (^2) _apt_

##### • E

##### [

```
ej^2 πf^1 ( ξ [ n + k ]− ξ [ n ])
```
##### ]

```
= e −^4 π
```
(^2) _f_ (^21) _σ_ (^2) _apt_
+ _δ_ ( _k_ )(1− _e_ −^4 _π_
(^2) _f_ 12 _σapt_ 2
)
So, the autocorrelation function of jitter noise becomes :
_Ree_ ( _k_ ) =

##### ∫+∞

```
−∞
```
```
Sxx ( f 1 ) exp( j 2 πf 1 kTs )
[
(1− e −^2 π
```
(^2) _f_ 12 _σ_ (^2) _apt_
)^2 + _δ_ ( _k_ )(1− _e_ −^4 _π_
(^2) _f_ (^21) _σ_ (^2) _apt_
)

##### ]

```
d f 1
```
And we deduce the power spectral density of jitter noise by taking the DTFT
of the autocorrelation function :

_Sjitter_ _ _apt_ ( _f_ ) =

```
F requency dependent component
︷ ︸︸ ︷
Sxx ( f )(1− e −^2 π
```
(^2) _f_ (^2) _σapt_ 2
)^2 +
_W hite component_
︷ ︸︸ ︷
1
_fs_

##### ∫+∞

```
−∞
```
```
Sxx ( f 1 )(1− e −^4 π
```
(^2) _f_ 12 _σapt_ 2
) d _f_ 1
(E.2)

### E.4 PSD of sampling noise due to clock jitter of a free-running oscillator

For a free-running oscillator, there is an accumulation of clock jitter with time.
So we have the following properties :

- _ξ_ [ _n_ ]∼N(0 _, nσ_^2 _clk_ )
- E

##### [

```
ej^2 πf^1 ξ [ n ]
```
##### ]

```
= e −^2 π
```
(^2) _f_ 12 _nσ_ (^2) _clk_

##### • E

##### [

```
ej^2 πf ( ξ [ n + k ]− ξ [ n ])
```
##### ]

```
= e −^2 π
```
(^2) _f_ (^2) | _k_ | _σ_ (^2) _clk_
When _n_ →+∞, _e_ −^2 _π_
(^2) _f_ 12 _nσclk_ 2
→+0, the jitter noise becomes stationnary
and its autocorrelation is :
_Ree_ ( _k_ )≃

##### ∫+∞

```
−∞
```
```
Sxx ( f 1 ) exp( j 2 πf 1 kTs )
[
(1 + e −^2 π
```
(^2) _f_ (^21) | _k_ | _σ_ (^2) _clk_ ]
d _f_ 1
We deduce the power spectral density of clock jitter for a free-running oscil-
lator :
_Sjitter_ _ _clk_ ( _f_ ) = _Sxx_ ( _f_ ) +
_Lorentzian spectrum_
︷∫ ︸︸ ︷
+∞
−∞
_Sxx_ ( _f_ 1 )
( _f_ 1 _σclk_ )^2 _fs
π_^2 ( _f_ 1 _σclk_ )^4 _fs_^2 + ( _f_ − _f_ 1 )^2
d _f_ 1 (E.3)


