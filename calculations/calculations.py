import math


## Medical dosage and Administration calculations ##
def dosage_by_weight(dose_per_kg: float, weight: float) -> float:
 """
 Calculates the appropriate drug dosage based on a patient's weight.
 Formula: Dosage = Dose per kg × Weight (kg)
 """
 return dose_per_kg * weight


def iv_flow_rate(volume: float, time: float) -> float:
 """
 Calculates the IV flow rate in mL per hour for proper administration.
 Formula: Flow Rate (mL/hr) = Volume (mL) / Time (hr)
 """
 return volume / time


def drip_rate(volume: float, drop_factor: float, time: float) -> float:
 """
 Calculates the number of drops per minute for an IV infusion.
 Formula: Drip Rate (gtt/min) = (Volume (mL) × Drop factor (gtt/mL)) / Time (min)
 """
 return (volume * drop_factor) / time


def medication_dose(desired_dose: float, volume: float, stock_strength: float) -> float:
 """
 Calculates the required dose based on available concentration.
 Formula: Dose = (Desired dose × Volume) / Stock strength
 """
 return (desired_dose * volume) / stock_strength


def insulin_dose(current_glucose: float, target_glucose: float, correction_factor: float) -> float:
 """
 Calculates insulin dose based on blood glucose levels and correction factor.
 Formula: Insulin dose = (Current glucose - Target glucose) / Correction factor
 """
 return (current_glucose - target_glucose) / correction_factor


def pediatric_dosage_youngs_rule(age: float, adult_dose: float) -> float:
 """
 Calculates pediatric drug dose using Young's Rule.
 Formula: Pediatric Dose = (Age ÷ (Age + 12)) × Adult Dose
 """
 return (age / (age + 12)) * adult_dose


def pediatric_dosage_clarks_rule(weight_lb: float, adult_dose: float) -> float:
 """
 Calculates pediatric drug dose using Clark's Rule.
 Formula: Pediatric Dose = (Weight (lb) ÷ 150) × Adult Dose
 """
 return (weight_lb / 150) * adult_dose


def creatinine_clearance(age: float, weight: float, serum_creatinine: float, is_female: bool) -> float:
 """
 Estimates creatinine clearance for medication dosing in patients with renal impairment.
 Formula: CrCl (mL/min) = [(140 - Age) × Weight (kg) × (0.85 if female)] / (72 × Serum Creatinine (mg/dL))
 """
 factor = 0.85 if is_female else 1
 return ((140 - age) * weight * factor) / (72 * serum_creatinine)


def heparin_infusion_rate(units_per_hour: float, concentration: float) -> float:
 """
 Calculates the required heparin infusion rate.
 Formula: Rate (mL/hr) = (Units/hr ordered ÷ Concentration (units/mL))
 """
 return units_per_hour / concentration


def fluid_maintenance_pediatrics(weight: float) -> float:
 """
 Calculates the fluid maintenance requirement for pediatric patients.
 Formula: Total Fluid (mL/hr) = 4mL/kg for first 10kg + 2mL/kg for next 10kg + 1mL/kg for remaining weight
 """
 if weight <= 10:
  return weight * 4
 elif weight > 10 and weight <= 20:
  return 40 + (weight - 10) * 2
 else:
  return 60 + (weight - 20) * 1


def apgar_score(appearance: int, pulse: int, grimace: int, activity: int, respiration: int) -> int:
 """
 Calculates newborn health status based on appearance, pulse, grimace, activity, and respiration.
 Formula: APGAR Score = Sum of 5 criteria scored 0-2 each
 """
 return appearance + pulse + grimace + activity + respiration


def oxygen_flow_rate(fio2: float, minute_ventilation: float) -> float:
 """
 Calculates the required oxygen flow rate based on desired FiO2.
 Formula: Flow Rate (L/min) = (FiO2 × Minute Ventilation) / 21
 """
 return (fio2 * minute_ventilation) / 21


def anion_gap(na: float, k: float, cl: float, hco3: float) -> float:
 """
 Calculates the anion gap to assess acid-base balance.
 Formula: Anion Gap = (Na+ + K+) - (Cl- + HCO3-)
 """
 return (na + k) - (cl + hco3)

## End of Medical dosage and Administration calculations ##

## Patient Monitoring calculations ##

def early_warning_score(respiratory_rate: float, oxygen_saturation: float, temperature: float, systolic_bp: float, heart_rate: float) -> float:
 """
 Calculates an early warning score based on vital signs to identify patient deterioration.
 Formula: EWS = Sum of scores for respiratory rate, oxygen saturation, temperature, systolic blood pressure, and heart rate
 """
 return respiratory_rate + oxygen_saturation + temperature + systolic_bp + heart_rate


def respiratory_rate_to_tidal_volume_ratio(respiratory_rate: float, tidal_volume: float) -> float:
 """
 Calculates the ratio of respiratory rate to tidal volume for assessing respiratory efficiency.
 Formula: RR/TV Ratio = Respiratory Rate / Tidal Volume
 """
 return respiratory_rate / tidal_volume


def shock_index(heart_rate: float, systolic_bp: float) -> float:
 """
 Calculates the shock index to assess hemodynamic stability.
 Formula: Shock Index = Heart Rate / Systolic Blood Pressure
 """
 return heart_rate / systolic_bp


def glasgow_coma_scale(eye_response: int, verbal_response: int, motor_response: int) -> int:
 """
 Calculates the Glasgow Coma Scale score to assess consciousness level.
 Formula: GCS = Eye Response + Verbal Response + Motor Response
 """
 return eye_response + verbal_response + motor_response


def pulse_pressure(systolic_bp: float, diastolic_bp: float) -> float:
 """
 Calculates the pulse pressure to assess cardiovascular health.
 Formula: Pulse Pressure = Systolic Blood Pressure - Diastolic Blood Pressure
 """
 return systolic_bp - diastolic_bp


def mean_arterial_pressure(systolic_bp: float, diastolic_bp: float) -> float:
 """
 Calculates mean arterial pressure to assess perfusion.
 Formula: MAP = [(2 × Diastolic) + Systolic] / 3
 """
 return ((2 * diastolic_bp) + systolic_bp) / 3


def oxygenation_index(fio2: float, mean_airway_pressure: float, pao2: float) -> float:
 """
 Calculates the oxygenation index to assess the severity of hypoxemia.
 Formula: OI = (FiO2 × Mean Airway Pressure × 100) / PaO2
 """
 return (fio2 * mean_airway_pressure * 100) / pao2

## End of Patient Monitoring calculations ##

## Nutrition and fluid management calculations ##

def daily_caloric_needs(bmr: float, activity_factor: float) -> float:
 """
 Calculates the daily caloric needs based on weight, height, age, and activity level.
 Formula: Calories (kcal/day) = BMR × Activity Factor
 """
 return bmr * activity_factor


def fluid_requirement_by_body_weight(weight: float) -> float:
 """
 Calculates daily fluid requirement based on body weight.
 Formula: Fluid (mL/day) = Weight (kg) × 30 mL
 """
 return weight * 30


def enteral_nutrition_formula(caloric_needs: float, formula_caloric_density: float) -> float:
 """
 Calculates the required volume of enteral nutrition formula to meet caloric needs.
 Formula: Volume (mL) = Caloric Needs (kcal) / Formula Caloric Density (kcal/mL)
 """
 return caloric_needs / formula_caloric_density


def parenteral_nutrition_macronutrient_distribution(total_calories: float, macronutrient_percentage: float) -> float:
 """
 Calculates the distribution of macronutrients in parenteral nutrition.
 Formula: Macronutrient Distribution = Total Calories × Macronutrient Percentage
 """
 return total_calories * macronutrient_percentage


def electrolyte_requirements(weight: float, requirement_factor: float) -> float:
 """
 Calculates daily electrolyte requirements based on weight.
 Formula: Electrolyte (mEq/day) = Weight (kg) × Requirement Factor
 """
 return weight * requirement_factor


def body_mass_index(weight: float, height: float) -> float:
 """
 Calculates BMI to assess body weight relative to height.
 Formula: BMI = Weight (kg) / (Height (m)²)
 """
 return weight / (height ** 2)


def caloric_requirements_harris_benedict(bmr: float, activity_factor: float) -> float:
 """
 Calculates daily caloric needs based on basal metabolic rate (BMR) and activity level.
 Formula: Calories = BMR × Activity Factor
 """
 return bmr * activity_factor


def tube_feeding_rate(total_volume: float, feeding_duration: float) -> float:
 """
 Calculates the required rate for enteral feeding.
 Formula: Rate (mL/hr) = Total Volume (mL) / Feeding Duration (hr)
 """
 return total_volume / feeding_duration


def fluid_replacement(deficit: float, maintenance: float) -> float:
 """
 Calculates the fluid replacement requirement based on deficit and maintenance needs.
 Formula: Total Fluid (mL) = Deficit (mL) + Maintenance (mL)
 """
 return deficit + maintenance


def protein_requirement(weight: float, protein_factor: float) -> float:
 """
 Calculates daily protein needs based on body weight.
 Formula: Protein (g/day) = Weight (kg) × Protein Factor (g/kg)
 """
 return weight * protein_factor


def daily_water_requirement(weight: float) -> float:
 """
 Calculates the daily water requirement based on body weight.
 Formula: Water (mL/day) = Weight (kg) × 40 mL
 """
 return weight * 40

## End of Nutrition and fluid management calculations ##

## Pharmacokinetics calculations ##

def half_life(volume_of_distribution: float, clearance: float) -> float:
 """
 Calculates the time required for the drug concentration to reduce by half.
 Formula: Half-Life (t½) = (0.693 × Volume of Distribution) / Clearance
 """
 return (0.693 * volume_of_distribution) / clearance


def clearance(dose: float, bioavailability: float, auc: float) -> float:
 """
 Calculates the clearance rate of a drug from the body.
 Formula: Clearance (L/time) = (Dose × Bioavailability) / Area Under the Curve (AUC)
 """
 return (dose * bioavailability) / auc


def volume_of_distribution(dose: float, plasma_concentration: float) -> float:
 """
 Calculates the apparent volume in which the drug is distributed.
 Formula: Volume of Distribution (L) = Dose / Plasma Concentration
 """
 return dose / plasma_concentration


def loading_dose(target_concentration: float, volume_of_distribution: float, bioavailability: float) -> float:
 """
 Calculates the initial dose required to achieve the desired plasma concentration.
 Formula: Loading Dose (mg) = Target Concentration × Volume of Distribution / Bioavailability
 """
 return (target_concentration * volume_of_distribution) / bioavailability


def maintenance_dose(clearance: float, target_concentration: float, bioavailability: float) -> float:
 """
 Calculates the dose required to maintain a steady-state concentration.
 Formula: Maintenance Dose (mg/time) = Clearance × Target Concentration / Bioavailability
 """
 return (clearance * target_concentration) / bioavailability


def steady_state_concentration(dose_rate: float, bioavailability: float, clearance: float) -> float:
 """
 Calculates the steady-state concentration of a drug during continuous dosing.
 Formula: Steady-State Concentration (mg/L) = (Dose Rate × Bioavailability) / Clearance
 """
 return (dose_rate * bioavailability) / clearance


def elimination_rate_constant(clearance: float, volume_of_distribution: float) -> float:
 """
 Calculates the rate constant for drug elimination.
 Formula: Elimination Rate Constant (k) = Clearance / Volume of Distribution
 """
 return clearance / volume_of_distribution


def area_under_curve(dose: float, bioavailability: float, clearance: float) -> float:
 """
 Calculates the total drug exposure over time.
 Formula: AUC (mg·time/L) = Dose × Bioavailability / Clearance
 """
 return (dose * bioavailability) / clearance


def time_to_steady_state(half_life: float) -> float:
 """
 Calculates the time required to reach steady-state concentration during continuous dosing.
 Formula: Time to Steady State = 5 × Half-Life
 """
 return 5 * half_life


def accumulation_factor(elimination_rate_constant: float, dosing_interval: float) -> float:
 """
 Calculates the accumulation factor for a drug given its dosing interval and half-life.
 Formula: Accumulation Factor = 1 / (1 - e^(-k × τ))
 """
 return 1 / (1 - math.exp(-elimination_rate_constant * dosing_interval))


def peak_plasma_concentration(dose: float, bioavailability: float, volume_of_distribution: float) -> float:
 """
 Calculates the peak plasma concentration after a single dose.
 Formula: Cmax = (Dose × Bioavailability) / (Volume of Distribution)
 """
 return (dose * bioavailability) / volume_of_distribution


def trough_plasma_concentration(peak_concentration: float, elimination_rate_constant: float, dosing_interval: float) -> float:
 """
 Calculates the trough plasma concentration before the next dose.
 Formula: Cmin = Cmax × e^(-k × τ)
 """
 return peak_concentration * math.exp(-elimination_rate_constant * dosing_interval)


def therapeutic_index(td50: float, ed50: float) -> float:
 """
 Calculates the therapeutic index of a drug to assess its safety margin.
 Formula: Therapeutic Index = TD50 / ED50
 """
 return td50 / ed50


def loading_dose_adjustment(target_concentration: float, adjusted_volume_of_distribution: float) -> float:
 """
 Calculates the adjusted loading dose for a patient with altered pharmacokinetics.
 Formula: Adjusted Loading Dose = Target Concentration × Adjusted Volume of Distribution
 """
 return target_concentration * adjusted_volume_of_distribution

## End of Pharmacokinetics calculations ##

## Blood and Lab Values calculations ##

def hemoglobin_to_hematocrit(hemoglobin: float) -> float:
 """
 Estimates hematocrit percentage from hemoglobin concentration.
 Formula: Hematocrit (%) = Hemoglobin (g/dL) × 3
 """
 return hemoglobin * 3


def red_cell_distribution_width(sd_rbc_volume: float, mean_corpuscular_volume: float) -> float:
 """
 Calculates the variation in red blood cell size.
 Formula: RDW (%) = (Standard Deviation of RBC Volume / Mean Corpuscular Volume) × 100
 """
 return (sd_rbc_volume / mean_corpuscular_volume) * 100


def reticulocyte_production_index(reticulocyte_count: float, hematocrit: float, normal_hematocrit: float, maturation_factor: float) -> float:
 """
 Adjusts the reticulocyte count for anemia severity.
 Formula: RPI = (Reticulocyte Count × Hematocrit) / (Normal Hematocrit × Maturation Factor)
 """
 return (reticulocyte_count * hematocrit) / (normal_hematocrit * maturation_factor)


def mean_platelet_volume(platelet_volume: float, platelet_count: float) -> float:
 """
 Calculates the average size of platelets in the blood.
 Formula: MPV (fL) = Platelet Volume / Platelet Count
 """
 return platelet_volume / platelet_count


def neutrophil_to_lymphocyte_ratio(neutrophil_count: float, lymphocyte_count: float) -> float:
 """
 Calculates the ratio of neutrophils to lymphocytes as an inflammatory marker.
 Formula: NLR = Neutrophil Count / Lymphocyte Count
 """
 return neutrophil_count / lymphocyte_count


def corrected_reticulocyte_count(reticulocyte_count: float, patient_hematocrit: float, normal_hematocrit: float) -> float:
 """
 Adjusts the reticulocyte count for anemia.
 Formula: Corrected Reticulocyte Count (%) = Reticulocyte Count × (Patient's Hematocrit / Normal Hematocrit)
 """
 return reticulocyte_count * (patient_hematocrit / normal_hematocrit)


def corrected_calcium(measured_calcium: float, albumin: float) -> float:
 """
 Adjusts calcium level based on albumin concentration.
 Formula: Corrected Calcium (mg/dL) = Measured Calcium + 0.8 × (4 - Albumin)
 """
 return measured_calcium + 0.8 * (4 - albumin)


def anion_gap(na: float, k: float, cl: float, hco3: float) -> float:
 """
 Calculates the anion gap to assess acid-base balance.
 Formula: Anion Gap = (Na+ + K+) - (Cl- + HCO3-)
 """
 return (na + k) - (cl + hco3)


def egfr(serum_creatinine: float, age: float, sex: str, race: str) -> float:
 """
 Estimates kidney function based on serum creatinine, age, sex, and race.
 Formula: eGFR (mL/min/1.73m²) = 186 × (Serum Creatinine)^-1.154 × (Age)^-0.203 × Sex Factor × Race Factor

 Sex Factor:
  - Male: 1.0
  - Female: 0.742

 Race Factor:
  - Black: 1.212
  - Non-Black: 1.0
 """
 sex_factor = 0.742 if sex.lower() == "female" else 1.0
 race_factor = 1.212 if race.lower() == "black" else 1.0

 return 175 * (serum_creatinine ** -1.154) * (age ** -0.203) * sex_factor * race_factor


def mean_corpuscular_volume(hematocrit: float, rbc_count: float) -> float:
 """
 Calculates the average volume of red blood cells.
 Formula: MCV (fL) = (Hematocrit × 10) / RBC Count
 """
 return (hematocrit * 10) / rbc_count


def transferrin_saturation(serum_iron: float, total_iron_binding_capacity: float) -> float:
 """
 Calculates transferrin saturation to assess iron status.
 Formula: Transferrin Saturation (%) = (Serum Iron / Total Iron Binding Capacity) × 100
 """
 return (serum_iron / total_iron_binding_capacity) * 100

## End of Blood and Lab Values calculations ##

## Cardiovascular Health calculations ##

def cardiac_output(stroke_volume: float, heart_rate: float) -> float:
 """
 Calculates cardiac output based on stroke volume and heart rate.
 Formula: Cardiac Output (L/min) = Stroke Volume (mL) × Heart Rate (bpm) / 1000
 """
 return (stroke_volume * heart_rate) / 1000


def stroke_volume(end_diastolic_volume: float, end_systolic_volume: float) -> float:
 """
 Calculates stroke volume based on end-diastolic and end-systolic volumes.
 Formula: Stroke Volume (mL) = End-Diastolic Volume (mL) - End-Systolic Volume (mL)
 """
 return end_diastolic_volume - end_systolic_volume


def mean_arterial_pressure(systolic_bp: float, diastolic_bp: float) -> float:
 """
 Calculates mean arterial pressure to assess perfusion.
 Formula: MAP = [(2 × Diastolic) + Systolic] / 3
 """
 return ((2 * diastolic_bp) + systolic_bp) / 3


def systemic_vascular_resistance(map_value: float, cvp: float, cardiac_output: float) -> float:
 """
 Calculates systemic vascular resistance to assess afterload.
 Formula: SVR (dyn·s/cm⁵) = [(MAP - CVP) × 80] / Cardiac Output
 """
 return ((map_value - cvp) * 80) / cardiac_output


def pulse_pressure(systolic_bp: float, diastolic_bp: float) -> float:
 """
 Calculates the pulse pressure to assess cardiovascular health.
 Formula: Pulse Pressure = Systolic Blood Pressure - Diastolic Blood Pressure
 """
 return systolic_bp - diastolic_bp


def ejection_fraction(stroke_volume: float, end_diastolic_volume: float) -> float:
 """
 Calculates the ejection fraction to assess heart function.
 Formula: Ejection Fraction (%) = (Stroke Volume / End-Diastolic Volume) × 100
 """
 return (stroke_volume / end_diastolic_volume) * 100


def cardiac_index(cardiac_output: float, body_surface_area: float) -> float:
 """
 Calculates the cardiac index to assess cardiac output relative to body surface area.
 Formula: Cardiac Index (L/min/m²) = Cardiac Output (L/min) / Body Surface Area (m²)
 """
 return cardiac_output / body_surface_area


def left_ventricular_stroke_work_index(map_value: float, pcwp: float, stroke_volume_index: float) -> float:
 """
 Calculates the left ventricular stroke work index to assess cardiac performance.
 Formula: LVSWI (g·m/m²) = (MAP - PCWP) × Stroke Volume Index × 0.0136
 """
 return (map_value - pcwp) * stroke_volume_index * 0.0136


def rate_pressure_product(heart_rate: float, systolic_bp: float) -> float:
 """
 Calculates the rate pressure product to assess myocardial oxygen demand.
 Formula: RPP = Heart Rate × Systolic Blood Pressure
 """
 return heart_rate * systolic_bp


def fractional_shortening(lvedd: float, lvesd: float) -> float:
 """
 Calculates fractional shortening to assess left ventricular function.
 Formula: Fractional Shortening (%) = [(LVEDD - LVESD) / LVEDD] × 100
 """
 return ((lvedd - lvesd) / lvedd) * 100


def qtc_interval(qt_interval: float, rr_interval: float) -> float:
 """
 Calculates the corrected QT interval for heart rate.
 Formula: QTc (ms) = QT Interval / √(RR Interval)
 """
 return qt_interval / math.sqrt(rr_interval)

## End of Cardiovascular Health calculations ##

## Body Mechanisms and Growth calculations ##

def body_water_percentage(weight: float, is_male: bool) -> float:
 """
 Estimates the total body water percentage based on weight and sex.
 Formula: Body Water (%) = (0.6 × Weight for males, 0.5 × Weight for females)
 """
 factor = 0.6 if is_male else 0.5
 return factor * weight


def bone_mineral_density(bone_mass: float, bone_area: float) -> float:
 """
 Calculates bone mineral density to assess bone health.
 Formula: BMD (g/cm²) = Bone Mass / Bone Area
 """
 return bone_mass / bone_area


# def metabolic_age(bmr: float, age: int) -> int:
#  """
#  Estimates metabolic age based on BMR and age.
#  Formula: Metabolic Age = Age adjusted to match BMR
#  """
#  return int(age)  # Placeholder, as actual calculation depends on a reference table


def waist_to_hip_ratio(waist_circumference: float, hip_circumference: float) -> float:
 """
 Calculates the waist-to-hip ratio to assess body fat distribution.
 Formula: Waist-to-Hip Ratio = Waist Circumference / Hip Circumference
 """
 return waist_circumference / hip_circumference


def growth_hormone_dosage(weight: float, dosage_factor: float, bsa: float = None) -> float:
 """
 Calculates the dosage of growth hormone based on weight or body surface area.
 Formula: Dosage (mg/day) = Weight (kg) × Dosage Factor or BSA × Dosage Factor
 """
 if bsa:
  return bsa * dosage_factor
 return weight * dosage_factor


def total_energy_expenditure(bmr: float, activity_factor: float) -> float:
 """
 Calculates the total energy expenditure based on BMR and activity level.
 Formula: TEE (kcal/day) = BMR × Activity Factor
 """
 return bmr * activity_factor


def body_surface_area(height: float, weight: float) -> float:
 """
 Calculates the body surface area based on height and weight, often used for determining chemotherapy dosage.
 Formula: BSA (m²) = √[(height (cm) × weight (kg)) / 3600]
 """
 return math.sqrt((height * weight) / 3600)


def lean_body_mass(weight: float, body_fat_percentage: float) -> float:
 """
 Calculates lean body mass based on weight and body fat percentage.
 Formula: LBM (kg) = Weight × (1 - Body Fat Percentage / 100)
 """
 return weight * (1 - body_fat_percentage / 100)


def growth_velocity(height_start: float, height_end: float, time_period: float) -> float:
 """
 Calculates the growth velocity over a specific time period.
 Formula: Growth Velocity (cm/year) = (Height at End - Height at Start) / Time Period
 """
 return (height_end - height_start) / time_period


def basal_metabolic_rate(weight: float, height: float, age: int, is_male: bool) -> float:
 """
 Calculates the basal metabolic rate to estimate energy expenditure at rest.
 Formula: BMR (kcal/day) = 10 × Weight (kg) + 6.25 × Height (cm) - 5 × Age (years) + (5 if male, -161 if female)
 """
 gender_factor = 5 if is_male else -161
 return 10 * weight + 6.25 * height - 5 * age + gender_factor



def body_fat_percentage(bmi: float, age: int, is_male: bool) -> float:
 """
 Estimates body fat percentage using skinfold measurements or BMI.
 Formula: Body Fat (%) = (1.20 × BMI) + (0.23 × Age) - (10.8 × Sex) - 5.4 (Sex: 1 for male, 0 for female)
 """
 sex_factor = 10.8 if is_male else 0
 return (1.20 * bmi) + (0.23 * age) - sex_factor - 5.4


def resting_energy_expenditure(bmr: float, activity_factor: float) -> float:
 """
 Calculates the resting energy expenditure to estimate daily caloric needs.
 Formula: REE (kcal/day) = BMR × Activity Factor
 """
 return bmr * activity_factor

## End of Body Mechanisms and Growth calculations ##

## Infection Control and Epidemiology calculations ##

def basic_reproduction_number(contact_rate: float, transmission_probability: float, duration_of_infectiousness: float) -> float:
 """
 Estimates the average number of secondary infections caused by one infected individual in a fully susceptible population.
 Formula: R0 = (Contact Rate × Transmission Probability × Duration of Infectiousness)
 """
 return contact_rate * transmission_probability * duration_of_infectiousness


def effective_reproduction_number(r0: float, susceptible_population: float, total_population: float) -> float:
 """
 Estimates the average number of secondary infections caused by one infected individual in a partially immune population.
 Formula: Rt = R0 × (Susceptible Population / Total Population)
 """
 return r0 * (susceptible_population / total_population)


def infection_fatality_rate(number_of_deaths: int, total_infected_individuals: int) -> float:
 """
 Calculates the proportion of deaths among all infected individuals, including asymptomatic cases.
 Formula: IFR (%) = (Number of Deaths / Total Infected Individuals) × 100
 """
 return (number_of_deaths / total_infected_individuals) * 100


def serial_interval(time_secondary_case: float, time_primary_case: float) -> float:
 """
 Calculates the average time between successive cases in a chain of transmission.
 Formula: Serial Interval = Time of Symptom Onset in Secondary Case - Time of Symptom Onset in Primary Case
 """
 return time_secondary_case - time_primary_case


def quarantine_effectiveness(transmission_with_quarantine: float, transmission_without_quarantine: float) -> float:
 """
 Estimates the reduction in transmission due to quarantine measures.
 Formula: Effectiveness (%) = (1 - (Transmission with Quarantine / Transmission without Quarantine)) × 100
 """
 return (1 - (transmission_with_quarantine / transmission_without_quarantine)) * 100


def case_fatality_rate(number_of_deaths: int, number_of_confirmed_cases: int) -> float:
 """
 Calculates the proportion of deaths among confirmed cases of a disease.
 Formula: CFR (%) = (Number of Deaths / Number of Confirmed Cases) × 100
 """
 return (number_of_deaths / number_of_confirmed_cases) * 100


def attack_rate(number_of_ill_individuals: int, total_population_at_risk: int) -> float:
 """
 Calculates the proportion of individuals who become ill after exposure to a disease.
 Formula: Attack Rate (%) = (Number of Ill Individuals / Total Population at Risk) × 100
 """
 return (number_of_ill_individuals / total_population_at_risk) * 100


def incidence_rate(number_of_new_cases: int, population_at_risk: int, time_period: float) -> float:
 """
 Calculates the rate of new cases of a disease in a population over a specific time period.
 Formula: Incidence Rate = (Number of New Cases / Population at Risk) × Time
 """
 return (number_of_new_cases / population_at_risk) * time_period


def secondary_attack_rate(number_of_secondary_cases: int, number_of_exposed_contacts: int) -> float:
 """
 Calculates the proportion of secondary cases among contacts of primary cases.
 Formula: Secondary Attack Rate (%) = (Number of Secondary Cases / Number of Exposed Contacts) × 100
 """
 return (number_of_secondary_cases / number_of_exposed_contacts) * 100


def herd_immunity_threshold(r0: float) -> float:
 """
 Calculates the proportion of the population that needs to be immune to stop disease transmission.
 Formula: Herd Immunity Threshold (%) = (1 - (1 / R0)) × 100
 """
 return (1 - (1 / r0)) * 100


def prevalence_rate(number_of_existing_cases: int, total_population: int) -> float:
 """
 Calculates the proportion of individuals in a population who have a disease at a specific point in time.
 Formula: Prevalence Rate (%) = (Number of Existing Cases / Total Population) × 100
 """
 return (number_of_existing_cases / total_population) * 100


def doubling_time(growth_rate: float) -> float:
 """
 Calculates the time it takes for the number of cases to double.
 Formula: Doubling Time = ln(2) / Growth Rate
 """
 return math.log(2) / growth_rate

## End of Infection Control and Epidemiology calculations ##

## Electrolyte Replacement calculations ##

def sodium_deficit(desired_sodium: float, current_sodium: float, total_body_water: float) -> float:
 """
 Calculates the sodium deficit to correct hyponatremia.
 Formula: Sodium Deficit (mEq) = (Desired Sodium - Current Sodium) × Total Body Water
 """
 return (desired_sodium - current_sodium) * total_body_water


def chloride_replacement(desired_chloride: float, current_chloride: float, total_body_water: float) -> float:
 """
 Calculates the chloride replacement required to correct hypochloremia.
 Formula: Chloride Replacement (mEq) = (Desired Chloride - Current Chloride) × Total Body Water
 """
 return (desired_chloride - current_chloride) * total_body_water


def bicarbonate_replacement(base_deficit: float, total_body_water: float) -> float:
 """
 Calculates the bicarbonate replacement required to correct metabolic acidosis.
 Formula: Bicarbonate Replacement (mEq) = Base Deficit × Total Body Water
 """
 return base_deficit * total_body_water


def phosphate_correction_for_calcium(phosphate_replacement: float, correction_factor: float) -> float:
 """
 Adjusts phosphate replacement based on calcium levels to avoid precipitation.
 Formula: Adjusted Phosphate (mmol) = Phosphate Replacement × Correction Factor
 """
 return phosphate_replacement * correction_factor


def hyperkalemia_correction(current_potassium: float, target_potassium: float) -> float:
 """
 Calculates the reduction in potassium levels required to correct hyperkalemia.
 Formula: Potassium Reduction (mEq/L) = Current Potassium - Target Potassium
 """
 return current_potassium - target_potassium


def potassium_replacement(desired_potassium: float, current_potassium: float, total_body_potassium: float) -> float:
 """
 Calculates the potassium replacement required to correct hypokalemia.
 Formula: Potassium Replacement (mEq) = (Desired Potassium - Current Potassium) × Total Body Potassium
 """
 return (desired_potassium - current_potassium) * total_body_potassium


def calcium_correction_for_albumin(measured_calcium: float, albumin: float) -> float:
 """
 Adjusts calcium level based on albumin concentration.
 Formula: Corrected Calcium (mg/dL) = Measured Calcium + 0.8 × (4 - Albumin)
 """
 return measured_calcium + 0.8 * (4 - albumin)


def magnesium_replacement(desired_magnesium: float, current_magnesium: float, total_body_magnesium: float) -> float:
 """
 Calculates the magnesium replacement required to correct hypomagnesemia.
 Formula: Magnesium Replacement (mEq) = (Desired Magnesium - Current Magnesium) × Total Body Magnesium
 """
 return (desired_magnesium - current_magnesium) * total_body_magnesium


def phosphate_replacement(desired_phosphate: float, current_phosphate: float, total_body_phosphate: float) -> float:
 """
 Calculates the phosphate replacement required to correct hypophosphatemia.
 Formula: Phosphate Replacement (mmol) = (Desired Phosphate - Current Phosphate) × Total Body Phosphate
 """
 return (desired_phosphate - current_phosphate) * total_body_phosphate

## End of Electrolyte Replacement calculations ##

## Other Nursing informatics calculations ##

def burn_area_rule_of_nines(affected_areas: list) -> float:
 """
 Estimates the total body surface area (TBSA) affected by burns using the Rule of Nines.
 Formula: TBSA (%) = Sum of affected areas based on Rule of Nines
 """
 return sum(affected_areas)


def parkland_formula(weight: float, tbsa: float) -> float:
 """
 Calculates fluid resuscitation requirements for burn patients.
 Formula: Total Fluid (mL) = 4 × Weight (kg) × TBSA (%)
 """
 return 4 * weight * tbsa


def oxygen_delivery(cardiac_output: float, hemoglobin: float, sao2: float, pao2: float) -> float:
 """
 Calculates oxygen delivery to tissues.
 Formula: Oxygen Delivery (mL/min) = Cardiac Output × (1.34 × Hemoglobin × SaO2 + (PaO2 × 0.003))
 """
 return cardiac_output * (1.34 * hemoglobin * sao2 + (pao2 * 0.003))


def ideal_body_weight(height: float, is_male: bool) -> float:
 """
 Calculates the ideal body weight based on height and sex.
 Formula: IBW (kg) = 50 + 2.3 × (Height (in) - 60) for males, 45.5 + 2.3 × (Height (in) - 60) for females
 """
 base_weight = 50 if is_male else 45.5
 return base_weight + 2.3 * (height - 60)


def adjusted_body_weight(actual_weight: float, ideal_body_weight: float) -> float:
 """
 Calculates adjusted body weight for obese patients.
 Formula: ABW (kg) = IBW + 0.4 × (Actual Weight - IBW)
 """
 return ideal_body_weight + 0.4 * (actual_weight - ideal_body_weight)


def corrected_sodium(measured_sodium: float, glucose: float) -> float:
 """
 Adjusts sodium level for hyperglycemia.
 Formula: Corrected Sodium (mEq/L) = Measured Sodium + 0.016 × (Glucose - 100)
 """
 return measured_sodium + 0.016 * (glucose - 100)


def a_a_gradient(pao2: float, pao2_alveolar: float) -> float:
 """
 Calculates the alveolar-arterial oxygen gradient.
 Formula: A-a Gradient = PAO2 - PaO2
 """
 return pao2_alveolar - pao2


def fractional_excretion_of_sodium(urine_sodium: float, plasma_creatinine: float, plasma_sodium: float, urine_creatinine: float) -> float:
 """
 Assesses kidney function and differentiates between prerenal and intrinsic renal failure.
 Formula: FENa (%) = [(Urine Sodium × Plasma Creatinine) / (Plasma Sodium × Urine Creatinine)] × 100
 """
 return ((urine_sodium * plasma_creatinine) / (plasma_sodium * urine_creatinine)) * 100


def serum_osmolality(sodium: float, glucose: float, bun: float) -> float:
 """
 Calculates serum osmolality to assess hydration status.
 Formula: Serum Osmolality (mOsm/kg) = 2 × Sodium + Glucose / 18 + BUN / 2.8
 """
 return 2 * sodium + glucose / 18 + bun / 2.8


def winters_formula(hco3: float) -> float:
 """
 Predicts the expected PaCO2 in metabolic acidosis.
 Formula: Expected PaCO2 = (1.5 × HCO3-) + 8 ± 2
 """
 return (1.5 * hco3) + 8

## End of Other Nursing informatics calculations ##

## Statistical calculations ##

def sensitivity(true_positives: int, false_negatives: int) -> float:
 """
 Calculates the sensitivity of a diagnostic test.
 Formula: Sensitivity (%) = (True Positives / (True Positives + False Negatives)) × 100
 """
 return (true_positives / (true_positives + false_negatives)) * 100


def specificity(true_negatives: int, false_positives: int) -> float:
 """
 Calculates the specificity of a diagnostic test.
 Formula: Specificity (%) = (True Negatives / (True Negatives + False Positives)) × 100
 """
 return (true_negatives / (true_negatives + false_positives)) * 100


def positive_predictive_value(true_positives: int, false_positives: int) -> float:
 """
 Calculates the positive predictive value of a diagnostic test.
 Formula: PPV (%) = (True Positives / (True Positives + False Positives)) × 100
 """
 return (true_positives / (true_positives + false_positives)) * 100


def negative_predictive_value(true_negatives: int, false_negatives: int) -> float:
 """
 Calculates the negative predictive value of a diagnostic test.
 Formula: NPV (%) = (True Negatives / (True Negatives + False Negatives)) × 100
 """
 return (true_negatives / (true_negatives + false_negatives)) * 100


def accuracy(true_positives: int, true_negatives: int, false_positives: int, false_negatives: int) -> float:
 """
 Calculates the accuracy of a diagnostic test.
 Formula: Accuracy (%) = ((True Positives + True Negatives) / Total Cases) × 100
 """
 total_cases = true_positives + true_negatives + false_positives + false_negatives
 return ((true_positives + true_negatives) / total_cases) * 100


def prevalence(total_cases: int, population: int) -> float:
 """
 Calculates the prevalence of a condition in a population.
 Formula: Prevalence (%) = (Total Cases / Population) × 100
 """
 return (total_cases / population) * 100


def likelihood_ratio_positive(sensitivity: float, specificity: float) -> float:
 """
 Calculates the positive likelihood ratio of a diagnostic test.
 Formula: LR+ = Sensitivity / (1 - Specificity)
 """
 return sensitivity / (1 - specificity)


def likelihood_ratio_negative(sensitivity: float, specificity: float) -> float:
 """
 Calculates the negative likelihood ratio of a diagnostic test.
 Formula: LR- = (1 - Sensitivity) / Specificity
 """
 return (1 - sensitivity) / specificity


def odds_ratio(exposed_cases: int, exposed_controls: int, unexposed_cases: int, unexposed_controls: int) -> float:
 """
 Calculates the odds ratio to measure the association between exposure and outcome.
 Formula: OR = (Exposed Cases × Unexposed Controls) / (Exposed Controls × Unexposed Cases)
 """
 return (exposed_cases * unexposed_controls) / (exposed_controls * unexposed_cases)


def relative_risk(exposed_cases: int, exposed_total: int, unexposed_cases: int, unexposed_total: int) -> float:
 """
 Calculates the relative risk to measure the likelihood of an outcome in exposed vs unexposed groups.
 Formula: RR = (Exposed Cases / Exposed Total) / (Unexposed Cases / Unexposed Total)
 """
 return (exposed_cases / exposed_total) / (unexposed_cases / unexposed_total)


## End of Statistical calculations ##