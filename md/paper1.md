## Time-Interleaved

# Analog-To-Digital

## Converters:

## Status and Future Directions

ChristianVogel HakanJohansson

```
ChristianDopplerLaboratoryforNonlinearSignalProcessing DivisionofElectronics
Systems
```
```
SignalProcessingandSpeechCommunication
Laboratory Department
```
```
ofElectrical
Engineering
```
```
GrazUniversityofTechnology,Austria
LinkopingUniversity,
```
```
Sweden
```
```
Email:c.vogel@ieee.org Email:
hakanj@isy.liu.se
```
```
Abstract-We discuss time-interleaved
analog-to-digital
```
```
converters
fsM o27= TI-ADC
```
```
(ADCs) as aprime
example
```
```
of
merging analog
```
```
and
digital signal
```
```
processing.Atime-interleavedADC
(TI-ADC)
```
```
consistsofM
parallel
```
```
ADC
```
```
channelADCsthatalternatelytake
samples
```
```
fromthe
inputsignal,
```
```
where
l
```
```
the
sampling
```
```
ratecanbeincreased
by
```
```
thenumberofchannels
compared f7|1Y/l=
```
```
toasinglechannel.Werecallthe
advantages
```
```
oftime
interleaving
```
```
and
l
```
```
investigate
```
```
the
problems
```
```
involved.In
particular,
```
```
we
explain
```
```
theerror
```
```
analoginput
```
```
.
```
```
ADC
```
```
digitaloutput
```
```
behaviorofmismatchesamongthe
channels,
```
```
whichdistortthe
```
## output xd(t)T y[n]

```
signalandreducethesystemperformance
significantly,
```
```
and
provide
```
```
a fM
=
```
```
m
MUX)
```
```
conciseframeworkfor
dealing
```
```
withthem.Basedonthis
analysis,
```
```
we I
```
```
reviewtheprinciplepossibilitiesofcalibratingTI-ADCs,wherewe
point +
```
```
ADC
```
```
outthenecessitiesandadvantagesofdigitalenhancement.Tothis
end,
```
```
we
```
```
discussopenissuesofchannelmismatchidentificationaswellaschannel
```
fIM

```
=(M-1)
```
```
I
```
```
mismatchcorrection.
```
```
I
```
```
I.
INTRODUCTION-I
```
```
Since
analog-to-digital
```
```
converters
(ADCs) ultimately
```
```
limitthe
```
Fig.1.

```
Time-interleavedADC(TI-ADC)withMchannels.Eachchannel
```
```
performanceof
today's
```
```
communication
systems,high-speed,high- alternatelytakessamplesatarateMfromtheinputsignalxa(t).Atthe
```
```
resolution,andpower-awareADCsare
required
```
```
inorderto
comply multiplexer(MUX),
```
```
the
samples
```
```
fromtheM
parallel
```
```
channelsare
merged
```
```
withnewcommunicationstandards.Thisalsoleadstoanincreased intooneoutputchannelrunningatanMtimeshigherrate
fs.
```
```
demandfor
high-speed
```
```
and
high-resolutionsamplingsystems
```
```
inthe
```
```
measurementindustry[1].PresentADC
technologies
```
```
workontheir
```
```
limitsandcannotbe
properlypushedfurther,
```
```
sincethe
downscaling andthemultiplexer(MUX)torecombinethedigitaloutputsofthe
```
```
ofIC
technologies
```
```
to
deep
```
```
sub-micron
technologies
```
```
makes their
channels.Theconversionrateoftheoverallsystemis
increasedby
```
```
design
```
```
evenmoredifficult.
However,
```
```
theincreased
componentdensity thenumberofchannelsM.Itshouldbenoticedthateachchannel
```
```
of
digital
```
```
circuitsallowsfor
using
```
```
additional
chip
```
```
areawithsmall
hastodealwiththeentireinputsignalxa
(t),
```
```
and,therefore,the
```
```
additionalcosts
[2]. sample-and-holdsineachchannelhavetoresolvethefull
inputsignal
```
```
Onepossibilitytoovercometheseperformancelimitsistouse
bandwidth.
```
```
parallelism,i.e.,tosplittheinformationoftheanaloginputsignal From
atheoreticalpointofview,wecanincreasethesampling
```
```
intoseveralparallelchannels,toconvertthemindependently, and rateofaTI-ADC
bythenumberofchannelsthatworkinparallelin
```
```
finallytorecombinethemintoonedigitaloutputsignal.Intheory, thesystem.
Ideally,thesamplingratewouldlinearlyscalewiththe
```
```
whichwasintroducedbyPapoulis'GeneralizedSamplingExpansion
numberofchannels;however,channelmismatchesultimatelylimit
```
```
(GSE) [3], therearemany waysto splittheinformationofthe
theperformanceofTI-ADCs.Ontheonehand,thedownscalingof
```
```
inputsignal.Inpractice,onlyafewparallelmulti-channelsampling theIC
technologiescomplicates thematchingofthecomponents,
```
```
structures [4]havebeenfurtheranalyzed[5]-[7],wherethetime-
but,ontheotherhand,theincreasedcomponentdensityallowsfor
```
```
interleavedstructureisamongthemostpromisingonesforthefuture.
includingadditionaldigitalcomponentswithsmalladditionalcosts.
```
```
Theideaofatime-interleavedADC
(TI-ADC)
```
```
isthateachchannel
Therefore,wecanadddigitalcircuitstoovercometheproblemsof
```
```
ina
system
```
```
ofM
parallel
```
```
channels
alternately
```
```
takesone
sample, analogconvertercircuits[11].TI-ADCsconstituteaprimeexample
```
```
whereasthe
samplingfrequency
```
```
ofonechanneldoesnotneedto
ofsuchmergingtechnologies,where thetechnologycan
only be
```
```
fulfillthe
Nyquist
```
```
Criterion
[8].However,
```
```
wheninthe
digital
```
```
domain
properlypushedfurther,whenweconsiderdigitally
enhancedanalog
```
```
all
samplesmerge
```
```
intoone
sequence
```
```
weobtainanoverall
sampling circuits.
```
```
frequency
```
```
thatfulfillsthe
Nyquist
```
```
criterion.
Thus,sampling
```
```
withan
```
```
idealTI-ADCwithMchannelsis
equivalent
```
```
to
sampling
```
```
withan II.
```
```
CHANNEL
MISMATCHES
```
```
idealADCwith anMtimeshighersamplingrate.The channels EachchannelADCinaTI-ADChastechnologydependenterrors
```
```
ofaTI-ADCcanberealizedindifferentconvertertechnologiesto (e.g.,integralnonlinearityerrors,
clockjitter)likeasingle-channel
```
```
achieveforexamplehigh-rateandlow-powerADCs[9]orhigh-rate ADC,butdueto
componentmismatchesamongthechannels,ad-
```
```
andhigh-resolutionADCs[10].
ditionalerrors,calledmismatcherrors,areintroduced[12].Thisis
```
```
ThetypicalstructureofaTI-ADCisshowninFig.
1.Weseethe illustratedinFig.2,whereweseeaTI-ADCwithchannelmismatches
```
analoginputsignalXa(t),theMtime-interleavedparallelchannels, andwithoutchannelmismatchesforasinusoidalinputsignal.For

0-7803-9390-2/06/$20.
©C2006IEEE 3386 ISCAS 2006


```
0
02040
```
```
02 O 1
```
```
-40-~~~ -4 0 43Q
```
```
l
```
```
20 2 ~20Fig.4. SpectrumofaTl-ADC.Eachadditionalspectralcomponentisa
```
```
TI-ADC \shifted(bykM)copyoftheinputspectrumXa(jQ),whichisweighted
```
```
with co0 bythecomplextransferfunctionV (jQ).Furthermore,wehaveDiracdelta
```
```
mismatches 80abbreviationVX forVk(
-k)-
```
```
a -
```
0. 0).40.60.

```
I
```
```
Normalized
frequency
```
Fig.2. Ifwehadnomismatcheswewouldseeanoutputspectrumlikefor

asingle-channelADC.Assoonaswehavemismatches,weobtainadditional becalculatedbydevelopingtheDiracdeltadistributionin(2)intoa

spectralcomponents,whichsignificantlyreducetheTI-ADCperformance. continuousFourierseries,whichleadsusto

```
MT
Ys>JQ)T2~=kK
```
```
J
```
```
E V (Q-
```
M)XaK(iQ-ikM,)J' (3)

```
| ~
```
###### ~~~too yo(t)

lwhere1M-

M1/T, iT, < Vk(iQ)=M E Hm(jQ)em M, (4)

```
Q
```
###### yo,ev(t)

```
Withoutaninputsignalthesampledoutput,i.e.,offsetmismatches
```
##### xt,,(t)

##### IMT mT, E y,(t)nmy,only,is

### M~ ~

#### I

### +s[+t(M1T|M- n=o

```
60 Pulse atk
```
whichareweightedwhere

```
theFouriertransformof(5)gives
```
```
towIaY,(t) Z Ok(Q-7)
```
```
(6)
```
Fig.3. Linearmismatchmodelofatime-interleavedADCwithMchannels °

andadditionaloffsetsineachchannel. where

```
°Ok = omei M. (7)
```
```
m
```
```
O
```
matchedchannels,

```
we
obtain
```
```
an
outputspectrum
```
```
likeforasingle
```
```
ThefinaloutputiSthelinearcombinationof(3)and(6),thatis
```
channel ADC.
We

```
seethe
inputsignal, harmonics relatedtothe
```
inputsignal,i.e.,integralnonlinearity(INL)errors,andanoisefloor

```
Ys(jQ)
=tYs(jQ)
```
```
+YS°(jQ). (8)
```
determinedbythequantizationnoise,differentialnonlinearity(DNL)

```
Frm()t(8wecneogiefqucyd anchatrsis
```
errors, andjittereffects.Incontrast,wesee fortheTI-ADCwith

```
ofTADsTh
inusgalpetmXa()ishfedb
```
channel mismatches additional spectralcomponents in the output kQ

```
n egtdb h
orsonigmsac rnfrfnto
```
spectrum,
which

```
degradethesystem
```
```
performance. Vh (jQ),
```
```
which
isillustratedinFig.4.Themismatchtransferfunction
```
Tomodelchannelmismatcheswecanusethesimplifiedmodel Vk(jQ) isthe discreteFouriertransform

```
(DFT)ofthe frequency
```
showninFig.3.TheinputsignalgoestoMparallellinearfilters

byeresponses

```
Hm(jQ) ofthe channels. For matched channels, all
```
givenbH Q-A -fr()l shiftedspectralcomponentsbecomezero,sincethemismatchtransfer

Hm()-Am(Q)e (1) functioniszeroforallk 7 0,±M,±2M,...Theoutputdistortions

and

```
isthensampledinatime-interleavedmanner.Additionally,we causedbyoffsetmismatchesdonotdependontheinputsignal a
(t)c.
```
add Mli

```
offsets
°m
```
```
ineachchannel,whicharesampledinthesame Wetherefore obtain afixed output signalpattern atkQM thatis
```
way

```
aswell.ThesignalsYm(t)(sampledinputsignalsandoffsets)of weightedbythefactor
```
ik,

```
whichistheDFTamongtheoffsetsof
```
allchannelsaremergedintooneoutputstreamYs(t),whichbecomes allchannels.Ifalloffsetsareidenticalwewillhavenomismatches

afterquantizationthedigitaloutputsignal
y[n].

```
Todeterminethe butwecouldstillhaveanoveralloffseterror00.
```
Outputsignal
Ys(t),

```
we
separate
```
```
the
input
```
```
signalpartandtheoffset Fora generalanalysisofdynamic andstaticnonlinearity mis-
```
partandneglectthequantizationprocesstosimplifythemodel. matcheswecanusenonlinearhybridfilterbanks,whichunifyand

```
Withoutoffsetsthesampledoutput,i.e.,linearmismatchesonly, simplifythetreatmentofchannelmismatches[13].
```
canbewrittenas Intheliterature,twokindsoflinearmismatches,i.e.,gainmis-

```
M-1 oo
```
```
matchesandtimingmismatches,havebeentreatedextensively.The
```
```
Ys(t) =3(Xa(t)*hm(t)) /d (t-(m+nM)T8), (2) gainofanADCisoftendefinedasthemagnituderesponsefora
DC
```
```
m=0 00-oc) inputsignal,whichinournotationcorrespondsto
```
whereTwisthesampling

```
period.TheFouriertransformof(2)can thrn Hm(jO)=Am(JO). (9)
```

```
Signal
```
```
with
Signal
```
```
without
```
```
channelmismatches
```
```
channelmismatches cantunethematchingontheanalogsideorwecanreconstructthe
```
```
distortedsignalonthedigitalside.Itisalsopossibletocombineboth
```
```
approaches[21].
```
```
Digital calibrationisattractiveinmanyways.Thedigitalcali-
```
```
Tunechannel
```
###### Adapt

```
brationis,liketheprincipaltopologyofaTI-ADC,independent
```
```
properties
```
```
Iparameters
```
## xj(t) My[

```
j
```
## Normazefrequen]y yNomazefjequ.n].

```
fromtheusedchannelconverter
technology.Hence,
```
```
wecan
apply
```
```
TI-ADC
Digitalalgorithm thesame
```
digital

```
calibrationmethodtoTI-ADCswithdifferentchan-
```
```
I
f nelconvertertechnologies,sincetheTI-ADCenvironmentandthe
```
```
production
process
```
```
donot
directly
```
```
influencethe
functionality
```
```
ofthe
```
```
l______
```
```
--
```
```
mismatch
```
```
p d functionality
```
```
L-
```
```
identification
```
```
calibrationmethod.
```
```
analog digital
```
```
A. CorrectionMethods
```
```
Fig.5. PossibilitiestocalibrateaTI-ADC. Although thecorrectionofgainandoffsetmismatchesinthe
```
```
digitaldomainisquitesimple,sinceweonlyhavetoaddatmost
```
```
one adderand onemultipliertothesignalpathofeachchannel
```
Thus,thegainmismatchisthedeviationofthegains
gm

```
fromthe ADC,thecorrectionoftimingmismatches(linear-phasemismatches)
```
averagegainofallchannels.InpracticalTI-ADCdesigns,however, ismuchmoredifficult.In fact,itisasub-problemofthenon-

wehavetodealwithmagnitudemismatches.Tocompensateforthem, uniformsamplingproblem.ForTI-ADCstheproblemsimplifiesto

afirstsolutionistousesomekindofaveragemagnituderesponse periodicallynon-uniformsampledsignals,i.e.,thetimeshiftsAtm

foreachchanneloverthefrequencybandofinterestinsteadofDC exhibitaperiodicity,wherethetimeshiftsAtmaresmallcompared

gains. tothesamplingperiodT8.However,undertheconstraintofanon-

```
Thetimingmismatchisthedeviationfromtheaveragedlinear- chipimplementationtheproblembecomesdifficultagain.
```
phaseresponsesofthechannelsnormalizedbythefrequency.Tosee Forthetiming-mismatchproblemaccurate solutionshavebeen

this,wesplitthephaseresponsesintoalinearandanonlinearpart, foundin[19],[20],[22],[23],althoughonlyforsomeofthem[19],

```
i.e., [20]theimplementationonaTI-ADCchipismaintainable.However,
```
(m(Q)

```
=
tmQ+
>m(Q)m
```
```
(10) forchangingtimingmismatchestheusedreconstructionmethodhas
```
```
tobeeasilyadaptable.Thus,anopenquestionistofindreconstruction
```
wheretmQisthelinear-phaseresponse

```
overthefrequencybandof methodswheretheneededcoefficientscanbesimplyderivedfromthe
```
interest.Thetiming

```
mismatchAtmisthedeviationfromtheaveraged estimatedtimingmismatches.Afirstsolutiontothisproblemcanbe
```
andfrequencynormalized

```
linear-phaseresponse,i.e., foundin[21],[24].In[24]theauthorsshowthatbyusingfractional
```
1 M-1 delayfilterstheyonly

```
haveto
redesign
```
```
onecoefficientineachchannel
```
Atm

```
=
tm M
```
###### E

```
tm.
```
```
(11)
```
```
to
adapt
```
```
to
changedtiming
```
```
mismatchesandin
[21]
```
```
amethodwas
```
```
m
```
```
M=0 introducedwhichreordersthechannelsequenceinordertoachieve
```
Itshouldbenoticedthatwecantreataperture-delaymismatcheswith aspectrallyshapedoutputsignal.Unfortunately,bothmethodsneed

thismodelaswell.The
aperture-delay

```
mismatchisthedeviationfrom someamountofadditionaloversampling.
```
theidealsamplinginstantcausedbytime-shifted

```
clocksignals.This Therefore,thegoaloftimingmismatchcorrectionistofindanac-
```
delay

```
canbe
represented
```
```
byanequivalenttime-shift(linearphase curate,power-awaremethod,whichonlyneedsaslightoversampling
```
shift)

```
ofthe
inputsignal
```
```
ineachchannelwhichcanbeaccomplished andwhichcanbeeasily adaptedtochangingtimingmismatches.
```
bythelinearfiltersHm(jQ).

```
Iftheseproblemsare solved,magnitudeandnonlinear-phasemis-
```
```
matches(bandwidth
```
```
mismatches)willlimittheeffectiveresolution
```
```
III. CALIBRATIONOFCHANNELMISMATCHES
```
```
ofTI-ADCsandwillthereforehavetobecorrectedforafurther
```
```
Avoiding
```
```
mismatches isthemainconcernindesigningfastTI- improvement[18].
```
ADCs[9].Unfortunately,

```
shrinkingICtechnologiesandincreasing
```
```
B IdentificationM
```
clockratesmakecomponentmatchingevenmore

```
difficult.Further- ethods
```
more,thematchingisinfluencedbytime-variant

```
parameterssuchas Theidentification ofmismatch parametersisthemostcritical
```
temperatureorcomponentaging.Therefore,calibration

```
methodsfor componentinthechannelmismatch compensationprocessofTI-
```
TI-ADCshavebeenproposed,

```
whichtunethecomponentmatching, ADCs.Iftheidentifiedparametersarewrongeventhebestcorrection
```
e.g., [14], [15], or digitally correctthe distorted output

```
signal, methodcannotimprovetheTI-ADCperformance.
```
e.g.,[16]-[20].

```
Fortheidentificationofthechannelmismatcheswithspecialinput
```
```
InFig. 5 theprincipalcalibrationmethodsareillustrated.
```
```
Wesee signalswecanfindaccuratesolutions[18],[25],[26].Nevertheless,
```
aTI-ADCdrivenbyasinusoidalinputsignal

```
xa
(t).Attheoutput identification
```
```
withspecialinputsignalsissuitableformeasurement
```
oftheTI-ADC(y[n])weseethesampledspectrumofthesinusoidal applications withcalibrationcycles

```
butnotsuitableforcommuni-
```
inputsignalanddistortionscausedbychannelmismatches.

```
Inorderto cations systems,whereingeneralwe havenoextraduty cycles
```
reducethesedistortionswehavetoidentifythesignificantmismatch

```
forthecalibration.There,theidentificationhastobedoneduring
```
parameters.Thistaskismucheasiertorealizewhenweknowthe thenormaloperationoftheTI-ADC with

```
theonlyrestrictionof
```
inputsignalXa(t),whichisindicatedbyadashedarrowfromthe bandlimitedinputsignals.Forsinglecommunicationprotocols,we

identificationboxtotheinputsignal. Inmanycases,however,we canassumeparticularsignalstatistics,however,thetrendtowards

haveno orjustlittlestatisticalknowledge, e.g.,bandlimitationor softwaredefinedradio(SDR)doesnotallowsuchassumptions.

modulationtechnique,abouttheinputsignal.Thislittleknowledge Forgain and offsetmismatch identification wecan find some

makesitmuch moredifficultto obtainreliableestimates forthe methods [17], [27], [28]. Inmany cases, we obtain good offset

mismatch parameters.Ifthe mismatchparameters areknown,we and gain mismatch estimates with a simple comparison of the


averaged outputvaluesandtheaveragedoutputpoweramongall [11]A.vanRoermund,H.Hegt,P.Harpe,G.Radulov,A.Zanikopoulos,

channels. Unfortunately, suchmethodsarevulnerabletoaninput K.Doris,andP.Quinn, "SmartADandDAconverters,"inIEEE

signalcorrelationwiththeswitchingsequenceofthechannels,i.e., InternationalSymposiumonCircuitsandSystems,vol.6,May2005,

```
weolygtaimitdnuber fdfferntsmple fro eac chanel
```
```
pp.
```
```
4062-4065.
```
weonlygetalimitednumberofdifferentsamplesfromeachchannel [12] C.Vogel,"Theimpactofcombinedchannelmismatcheffectsintime-

fortheestimationprocess. interleavedADCs,"IEEETrans.onInstrumentationand
Measurement,

```
Themost challenging problemisthe on-lineidentification of
```
```
vol.54,no.1,
pp.
```
```
415-427,
February
```
```
2005.
```
timingmismatches. Theidentification shouldbe accurateand its

```
[13]C. VogelandG.Kubin, "Modeling
oftime-interleavedADCswith
```
```
nonlinearhybridfilterbanks,"AEU-InternationalJ.ofElectronicsand
```
```
implementationshouldbecost-efficient.Althoughwecanfind
identi-
```
```
Communications,
vol.
```
```
59,no.5,pp.288-296,
2005.
```
ficationmethodsintheliterature[17],[29],theyareeitherimprecise, [14]K.Dyer,F.Daihong,S.Lewis,andP.Hurst,"Ananalogbackground

limitedinthenumberofchannels,orhaveanenormouscomputa-

```
calibration
technique
```
```
fortime-interleaved
analog-to-digitalconverters,"
```
tionalcomplexity.

```
IEEEJ.ofSolid-StateCircuits,vol.33,no.12,pp.1912-1919,Decem-
```
```
Hencewe eedsableon-lieidntifcatio metodsfrofset,
```
```
ber1998.
```
```
Hence,weneedstableon-lineidentification methodsforoffset, [
```
15]

```
C.
```
Vogel,

```
D.
Draxelmayr,
```
```
and
```
```
FKuttner,"Compensationoftimingmis-
```
gain,andtimingmismatches,whereanaccurateandimplementation matchesintime-interleavedanalog-to-digitalconvertersthroughtransfer

efficienttimingmismatchidentificationistheforemostchallengefor characteristicstuning,"inProceedingsofthe47thIEEEInternational

thefuture.Afterhavingsolvedtheseproblems,however,wewill MidwestSymposiumOnCircuitsandSystems,vol. 1,July2004,pp.

alsohavetodealwiththeidentificationofbandwidthmismatches 341-344.

```
[16]H.JinandE.K.F.Lee,
```
```
"A
digital-backgroundcalibrationtechnique
```
andnonlinearitymismatches. forminimizingtiming-erroreffectsintime-interleavedADCs,"IEEE

```
Trans.onCircuitsand
Systems
```
```
II:
Analog
```
```
and
Digital
```
```
SignalProcessing,
```
```
IV. CONCLUSION vol.47,no.7,pp.603-613,July2000.
```
```
[17]S.Jamal,D.Fu,M.Singh,P.Hurst,andS.Lewis,"Calibrationof
```
```
Wehavepresentedaunifiedframeworkfordealingwithlinear sample-timeerrorinatwo-channeltime-interleavedanalog-to-digital
```
channel mismatches andoffsetmismatches. Inparticular,wecan

```
converter,"IEEETrans.onCircuitsand
Systems
```
```
I:
RegularPapers,
```
usethisframeworktodescribegainandtimingmismatches asa

```
vol.51,no.1,pp.130-139,January
2004.
```
```
[18]
```
```
M.Seo,M.Rodwell,andU.Madhow,
"Comprehensivedigital
```
```
correction
```
ofmismatcherrorsfora400-Msamples/s80-dBSFDRtime-interleaved

andidentificationofchannelmismatches andwehavepointedout analog-to-digitalconverter," IEEETrans.onMicrowave Theoryand

themostchallengingproblemsforthenearfuture.Sincethemajor Techniques,

```
vol.
53,
```
```
no.
3,pp.1072-1082,April
```
```
2005.
```
problemsofoffset,gain,andtimingmismatchcorrectionhavebeen

```
[19]H. Johanssonand P.
Lowenborg,
```
```
"Reconstruction ofnonuniformly
```
recentlysolved,themainconcernforthefuturewillbefindingstable

```
sampledbandlimitedsignalsbymeansoftime-varying
discrete-time
```
```
FIRfilters,"toappearinJ.AppliedSignalProcessing
```
-
    SpecialIssue

and reliableon-linemismatchidentificationmethods. However,to onFramesandOvercompleteRepresentations inSignalProcessing,

achieveveryhigh-resolutionTI-ADCsmoreerrors,e.g.,bandwidth Communications,andInformationTheory,2006.

mismatches, INLmismatches, andDNLmismatches,have tobe [20]

```
R.
Prendergast,
```
```
B.
Levy,
```
```
andP.Hurst,"Reconstructionof
band-limited
```
considered and calibratedaswell.Forexample, fora 100 MHz

```
periodicnonuniformlysampledsignalsthroughmultiratefilterbanks,"
```
signalbandwidth,a50MHDCbadiIEEE

```
Trans.onCircuitsandSystemsI:RegularPapers,vol.51,no.8,
```
signalbandwidth,a 750 MHzADCbandwidth,andananalogdevice pp.1612-1622,August2004.

matchingof1%,thebandwidthmismatchwilllimittheresolutionto [21]C.Vogel,D. Draxelmayr,andG.Kubin,"Spectralshapingoftimingmis-

some12-13bits.Theresearchonthesemismatcheshasjuststarted.

```
matchesintime-interleaved
analog-to-digitalconverters,"
```
```
in
Proceedings
```
```
of
```
```
the 2005 IEEEInternational
Symposium
```
```
onCircuitsand
Systems,May
```
```
REFERENCES
```
```
2005,pp.1394-1397.
```
```
[22]
```
```
Y C.
Jenq,
```
```
"Perfectreconstructionof
digitalspectrum
```
```
fromnonuni-
```
```
[1]K.Poulton,R.Neff,B.Setterberg,B.Wuppermann,T.Kopley,R.Jewett,
```
```
formlysampledsignals,"IEEETrans.onInstrumentationandMeasure-
```
```
J.Pernillo,C.Tan,andA.Montijo,"A 20 GS/s 8 bADCwitha 1 MB ment,vol.46, no.7,pp. 649 - 652,June1997.
```
```
memoryin0.18,umCMOS,"inIEEEInternationalSolid-StateCircuits
```
```
[23]YC.EldarandA.V.Oppenheim,"Filterbankreconstructionofbandlim-
```
```
Conference,vol.1,February2003,pp.318-496.
```
```
itedsignalsfromnonuniform
andgeneralizedsamples,"IEEETrans.on
```
```
[2]B.MurmannandB.E.Boser,DigitallyAssistedPipelineADCs:Theory SignalProcessing,vol.48,no.10,pp.2864-2875,October2000.
```
```
andImplementation. Springer,2004.
```
```
[24]H. Johanssonand P.
Lowenborg,
```
```
"Reconstruction ofnonuniformly
```
3 An "n z s e I s. X

```
sampledbandlimitedsignalsbymeansofdigitalfractionaldelayfilters,"
```
```
[3]A.Papoulis,"Generalizedsamplingexpansion,"IEEETrans.onCircuits IEETas nSga rcsig vl 0 o 1 p 77
77
```
```
and
Systems,
```
```
vol.
23,
```
```
no.
11,pp.
```
```
652-
654,
```
```
November1977.
```
```
IEEETrans.onSignalProcessing,vol.50,no.
```
11,

```
pp.2757-2767,
```
```
[4]J. J.Brown,"Multi-channelsamplingoflow-passsignals,"IEEETrans
```
```
November2002.
```
```
onCircuitsand
Systems,
```
```
vol.
28,
```
```
no.
2,pp.101-106,February
```
```
1981.
```
```
[25]
```
```
Y.C.
```
Jenq,

```
"Digitalspectra
```
```
of
nonuniformlysampledsignals:
```
```
Arobust
```
```
[5]A.PetragliaandS.K.Mitra,"High-speedA/Dconversionincorporating
```
```
samplingtimeoffsetestimationalgorithmforultrahigh-speedwaveform
```
```
digitizers usinginterleaving,"
```
```
IEEETrans. onInstrumentationand
```
```
aQMFbank," IEEETrans. onInstrumentationandMeasurement, Mesrmn,vl 9 o , p 17,Fbur 90
```
```
vol.41,no.3,pp.427-431,June1992.
```
```
Measurement,vol.39,no.1,pp.71-75,February1990.
```
```
[6]5. R.Velazquez,T. Q.Nguyen, andS. R. Broadstone,"Design of
```
```
[26]
```
```
J.
Pereira,
```
```
P.
Girao,
```
```
andA.
Serra,
```
```
"AnFFT-basedmethodtoevaluate
```
```
hybrifilterbanksforanalog/digital
conversion,"
```
```
IEEE
Trans.
```
```
onSignal
```
```
and
compensategain
```
```
andoffseterrorsofinterleavedADC
systems,"
```
```
hybridfilterbanksforanalog/digitalconversion,"IEEETrans.onSignal IE Trn.onIsrm tainndM suen,vl.5,o.2p.
```
```
Processing,vol.46,no.4,pp.956-967,April1998.
```
```
IEEE
Trasr
```
o strumentatnad

Measurernent,

```
vol.53,no.2,pp.
```
```
[7]
```
```
P.
Lowenborg,
```
```
H.
Johansson,
```
```
andL.
Wanhammar,
```
```
"Two-channel
digital
```
```
42
```
###### '3,Api

```
04
```
```
[7]P.dwebor,
```
..

JhnsnadL.

```
Wahmmr "Tochne diia
```
[27]D.Fu,K.C.Dyer,S.H.Lewis,andP.J.Hurst,"Adigitalbackground

```
and
hybridanalog/digital
```
```
multiratefilterbankswith
verylow-complexity
```
calibr.ationt ne forte-in

```
d
```
analog-to-digitalbackgoners

```
analysis
```
```
or
synthesisfilters,"
```
```
IEEETrans.onCircuitsand
Systems
```
II: iEEEJiofSolidteCircuitsvl.a33,

```
no
```
-1911,cem-

```
AnalogandDigitalSignalProcessing,vol.50,no.7,pp.355-367,July ber1998.
```
[28]V.Ferragina,A.Fornasari,U.Gatti,P.Malcovati,andF.Maloberti,

```
[8]
```
```
W.C.BlackJr.andD.A.
Hodges,
```
```
"Time-interleavedconverter
arrays,
"Gainandoffsetmismatchcalibrationintime-interleaved
multipath
```
```
A/D
```
```
I1 ,
sgma-deltamodulators,"
IEEETrans.onCircuits
```
```
andSystemsI:
Regular
```
```
190
```
```
Papers,vol.51,no.12,pp.2365-2373,December2004.
```
```
[9]D.Draxelmayr,"A6b600MHz 10mWADCarrayindigital9Onm [29] J.Elbornsson,F.Gustafsson,andJ.E.Eklund,"Blindadaptiveequal-
```
```
CMOS,"in 2004 IEEEInternationalSolid-StateCircuitsConference, izationofmismatcherrorsinatime-interleavedA/Dconvertersystem,"
```
```
vo.,erury204 ~
4-4.IEEETrans.onCircuitsandSystemsI:Regular
Papoers,
```
```
vol.51,no.1,
```
```
[10]M.KozakandI.Kale,OversampledDelta-SigmaModulators:Analysis,
p.1118 aur 04
```
```
ApplicationsandNovelTopologies. KluwerAcademicPublishers,2003. p.15-58Jaur
```

