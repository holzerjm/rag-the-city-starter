<!--
  Millbrook City RAG Challenge © William Caban — used with permission.
  All content is fictional, AI-generated synthetic data.
  Source: https://gist.github.com/williamcaban/8764f13aaa5c4b0768033671483f6c0f
  This corpus is NOT covered by this repository Apache-2.0 code license.
-->

# MILLBROOK RAG TESTING QUESTIONS

## CHALLENGE CATEGORY 1: AMBIGUOUS REFERENCES

### QUESTION 1A (Difficulty: Medium)
**Question:** "Who owns Romano's Bakery, and how is this person related to Isabella Romano?"

**Challenge:** Tests ability to distinguish between Isabella Romano (nursing student) and Rosa Romano (grandmother, bakery founder)

**Expected Answer:** Rosa Romano owns/founded Romano's Family Bakery in 1963. Isabella Romano is her granddaughter who lives with her.

**Wrong Answers a RAG might give:**
- Isabella Romano owns the bakery
- They are the same person
- No relationship established

---

### QUESTION 1B (Difficulty: Hard)
**Question:** "Dr. Okafor treated a patient in the emergency department. What was the patient's condition, and what is Dr. Okafor's relationship to the patient?"

**Challenge:** Tests disambiguation between Dr. Kwame Okafor (pediatrician) and Dr. Elena Vasquez's colleague also named "Dr. Okafor"

**Expected Answer:** Dr. Kwame Okafor (pediatrician) treated Emmanuel Okafor for acute appendicitis. Emmanuel is Dr. Okafor's son.

**Wrong Answers a RAG might give:**
- Confusing which Dr. Okafor
- Incorrect patient-doctor relationship
- Missing the family connection

---

### QUESTION 1C (Difficulty: Medium)
**Question:** "There are two bakeries mentioned in the documents. What are their names and who runs them?"

**Challenge:** Tests ability to identify and distinguish between Al-Rashid Mediterranean Bakery and Romano's Family Bakery

**Expected Answer:** Al-Rashid Mediterranean Bakery (run by Ahmed Al-Rashid) and Romano's Family Bakery (founded by Rosa Romano in 1963)

**Wrong Answers a RAG might give:**
- Only identifying one bakery
- Confusing the owners
- Missing the historical founding information

---

## CHALLENGE CATEGORY 2: TEMPORAL COMPLEXITY

### QUESTION 2A (Difficulty: Hard)
**Question:** "What significant infrastructure event happened in Millbrook in 1963, and how does it relate to current events in 2024?"

**Challenge:** Tests ability to connect historical events (bridge construction, bakery founding) with current crisis

**Expected Answer:** Bridge 7 was constructed in 1963 (same year Rosa Romano founded her bakery). In 2024, this bridge requires major structural repairs due to deterioration.

**Wrong Answers a RAG might give:**
- Missing the temporal connection
- Confusing construction vs. repair dates
- Not linking historical and current events

---

### QUESTION 2B (Difficulty: Medium)
**Question:** "How long has Ahmed Al-Rashid been operating his bakery, and what was his career before opening it?"

**Challenge:** Tests timeline calculation and career progression tracking

**Expected Answer:** Al-Rashid has been operating his bakery for 30 years (opened 1994, document dated 2024). Before that, he worked in construction after immigrating in 1989.

**Wrong Answers a RAG might give:**
- Incorrect timeline calculations
- Missing the immigration date
- Confusing pre-bakery career

---

### QUESTION 2C (Difficulty: Medium)
**Question:** "When did Dr. Elena Vasquez assume her current role as Hospital Director, and how long had she been at the hospital before that promotion?"

**Challenge:** Tests career progression timeline within the same institution

**Expected Answer:** She became Hospital Director in January 2020. She had been at Millbrook General since 2006, so 14 years before her promotion.

**Wrong Answers a RAG might give:**
- Confusing start date vs. promotion date
- Incorrect timeline calculations
- Missing the career progression details

---

## CHALLENGE CATEGORY 3: CONTRADICTORY INFORMATION

### QUESTION 3A (Difficulty: Hard)
**Question:** "What is the current load capacity of Bridge 7, and are there any restrictions in place?"

**Challenge:** Tests ability to identify and resolve conflicting load capacity information

**Expected Answer:** The current load rating is 25 tons (reduced from original 40 tons), but there are temporary 15-ton restrictions due to safety concerns.

**Wrong Answers a RAG might give:**
- Providing only one number without context
- Missing the temporary restrictions
- Not explaining the capacity reduction

---

### QUESTION 3B (Difficulty: Medium)
**Question:** "How much time will be added to emergency response times due to the bridge construction, and how has this actually affected hospital operations?"

**Challenge:** Tests ability to reconcile specific projections (+4.7 minutes) with general reports ("minimal impact")

**Expected Answer:** The engineering report projects +4.7 minutes average response time, but the newspaper reports actual increases have been "minimal" due to proactive routing strategies.

**Wrong Answers a RAG might give:**
- Only citing one source
- Not recognizing the apparent contradiction
- Missing the distinction between projected vs. actual impact

---

### QUESTION 3C (Difficulty: Hard)
**Question:** "What is the projected economic impact of the bridge construction on local businesses?"

**Challenge:** Tests handling of different economic impact measurements

**Expected Answer:** Two different measures are given: $47,000 per day economic loss (from detour costs), and 25-35% reduction in foot traffic for Historic Downtown businesses.

**Wrong Answers a RAG might give:**
- Only providing one metric
- Confusing the different types of economic impact
- Missing the distinction between general economic loss and specific business impact

---

## CHALLENGE CATEGORY 4: MISSING CONTEXT SCENARIOS

### QUESTION 4A (Difficulty: Medium)
**Question:** "What happened to Isabella Romano's parents?"

**Challenge:** Tests ability to recognize when information is not provided in the documents

**Expected Answer:** The documents indicate Isabella's parents are deceased but do not provide details about what happened to them.

**Wrong Answers a RAG might give:**
- Making up details not in the documents
- Claiming no information about parents is provided
- Confusing with other family information

---

### QUESTION 4B (Difficulty: Hard)
**Question:** "Why did Sofia Okafor move from Texas to Millbrook to start her engineering firm?"

**Challenge:** Tests recognition of missing contextual information about motivation

**Expected Answer:** The documents indicate Sofia has a Texas PE license and founded her firm in Millbrook in 2018, but do not explain the reason for relocating.

**Wrong Answers a RAG might give:**
- Fabricating reasons not in the text
- Not recognizing the Texas connection
- Missing the timeline of firm founding

---

### QUESTION 4C (Difficulty: Medium)
**Question:** "What architectural projects has Miguel Vasquez (Elena's husband) worked on in Millbrook?"

**Challenge:** Tests recognition when a person is mentioned but their professional work is not detailed

**Expected Answer:** Miguel Vasquez is identified as an architect and Elena's husband, but no specific projects in Millbrook are mentioned in the documents.

**Wrong Answers a RAG might give:**
- Inventing projects not mentioned
- Confusing with other construction/engineering work
- Missing that he's an architect

---

## CHALLENGE CATEGORY 5: DOMAIN CONFUSION

### QUESTION 5A (Difficulty: Medium)
**Question:** "What does Sofia Okafor's PE license enable her to do professionally?"

**Challenge:** Tests correct interpretation of "PE" as Professional Engineer vs. Physical Education

**Expected Answer:** Sofia's PE (Professional Engineer) license #89472 enables her to practice engineering and stamp engineering documents in Texas (she also has a California PE license #67821).

**Wrong Answers a RAG might give:**
- Confusing with Physical Education
- Not understanding professional licensing
- Missing the multi-state licensing aspect

---

### QUESTION 5B (Difficulty: Hard)
**Question:** "In the medical record, what does 'attending physician' refer to, and how does this differ from meeting attendance mentioned elsewhere?"

**Challenge:** Tests domain-specific terminology interpretation

**Expected Answer:** "Attending physician" refers to Dr. Kwame Okafor's role as the supervising doctor responsible for patient care, not meeting attendance. This is standard medical terminology.

**Wrong Answers a RAG might give:**
- Confusing with meeting attendance
- Not understanding medical hierarchy
- Missing the professional role distinction

---

### QUESTION 5C (Difficulty: Medium)
**Question:** "What type of 'code-switching' is mentioned in the documents?"

**Challenge:** Tests linguistic vs. programming context understanding

**Expected Answer:** Linguistic code-switching - the practice of alternating between languages within conversations, as shown in the bakery conversation transcript.

**Wrong Answers a RAG might give:**
- Relating to computer programming
- Missing the multilingual context
- Not understanding sociolinguistic terminology

---

## CHALLENGE CATEGORY 6: RELATIONSHIP COMPLEXITY

### QUESTION 6A (Difficulty: Hard)
**Question:** "How are Carmen Vasquez and Emmanuel Okafor connected, and trace the path of their relationship through their families' professional connections?"

**Challenge:** Tests multi-hop relationship reasoning across professional and personal domains

**Expected Answer:** Carmen Vasquez (daughter of Dr. Elena Vasquez) is friends with Emmanuel Okafor (son of Dr. Kwame Okafor). Their mothers work together at Millbrook General Hospital - Elena as Hospital Director and Kwame as a pediatrician.

**Wrong Answers a RAG might give:**
- Missing the family connections
- Not linking professional and personal relationships
- Confusing the hospital hierarchy

---

### QUESTION 6B (Difficulty: Hard)
**Question:** "What connections exist between the Chen family and the bridge project, considering both professional and personal relationships?"

**Challenge:** Tests ability to trace complex relationship networks across multiple contexts

**Expected Answer:** Marcus Chen (city councilman) works professionally with Sofia Okafor on the bridge project. His daughter Lily Chen is friends with Carmen Vasquez, whose mother (Dr. Elena Vasquez) has concerns about bridge impact on hospital access. Lily also helps Isabella Romano with studies, connecting to another affected family.

**Wrong Answers a RAG might give:**
- Only identifying direct professional connections
- Missing the student friendship networks
- Not connecting family relationships to professional issues

---

### QUESTION 6C (Difficulty: Hard)
**Question:** "How many degrees of separation exist between Ahmed Al-Rashid and Dr. Kwame Okafor, and what is the path?"

**Challenge:** Tests complex network analysis across multiple document types

**Expected Answer:** Multiple paths exist: 
1. Direct: Al-Rashid → community meetings → hospital discussions → Dr. Okafor
2. Through children: Al-Rashid → community connections → Emmanuel Okafor → Dr. Okafor (father)
3. Through Isabella: Al-Rashid → Isabella Romano (who knows about Emmanuel's hospital visit) → Dr. Okafor

**Wrong Answers a RAG might give:**
- Only finding one connection path
- Missing community network connections
- Not recognizing multiple relationship types

---

## CHALLENGE CATEGORY 7: MULTILINGUAL AND CULTURAL COMPLEXITY

### QUESTION 7A (Difficulty: Medium)
**Question:** "What languages does Dr. Elena Vasquez speak, and how do her language skills impact her role in the community?"

**Challenge:** Tests information synthesis across multiple documents and contexts

**Expected Answer:** Dr. Vasquez speaks Spanish (native), English (fluent), and Portuguese (conversational). Her bilingual abilities help in medical care and community meetings, as noted in Carmen's academic comments about tutoring Spanish-speaking students.

**Wrong Answers a RAG might give:**
- Missing some languages
- Not connecting language skills to professional/community impact
- Confusing with other multilingual characters

---

### QUESTION 7B (Difficulty: Hard)
**Question:** "In the bakery conversation transcript, identify all instances of code-switching and explain what languages are being mixed."

**Challenge:** Tests detailed linguistic analysis and cultural understanding

**Expected Answer:** Multiple instances:
- Ahmed: Arabic ("أهلاً وسهلاً" - welcome) to English
- Dr. Vasquez: Spanish ("Gracias," "Para los pacientes cardíacos") mixed with English
- Marcus: English to Mandarin ("你明白吗？") 
- Isabella: Italian ("Scusi," "questi ponti vengono e vanno") to Spanish/English
- Ahmed: Arabic ("المجتمع يجب أن يعرف") translated to English

**Wrong Answers a RAG might give:**
- Missing some code-switching instances
- Incorrect language identification
- Not understanding the cultural context

---

## CHALLENGE CATEGORY 8: TECHNICAL DOMAIN INTEGRATION

### QUESTION 8A (Difficulty: Hard)
**Question:** "According to the engineering report, what are the specific technical reasons Bridge 7 needs immediate attention, and how do these relate to the timeline concerns expressed in the city council meeting?"

**Challenge:** Tests integration of technical and policy information across document types

**Expected Answer:** Technical reasons include 15.3cm pylon displacement, 65% load capacity, micro-cracking, and 18% natural frequency reduction. These support the council's concern about the 8-14 month failure timeline and need for immediate $2.3M intervention.

**Wrong Answers a RAG might give:**
- Only citing general concerns without technical details
- Not connecting engineering data to policy discussions
- Missing the timeline correlation

---

### QUESTION 8B (Difficulty: Medium)
**Question:** "What medical considerations are mentioned regarding the bridge construction, and which healthcare professionals are involved in planning?"

**Challenge:** Tests cross-domain professional coordination

**Expected Answer:** Main concerns are increased emergency response times (+4.7 minutes) affecting cardiac patients. Dr. Elena Vasquez (Hospital Director) and Rebecca Martinez (Emergency Nurse Manager) are involved in planning alternative routes and weekly progress reviews.

**Wrong Answers a RAG might give:**
- Missing specific medical professionals
- Not identifying the cardiac patient concern
- Confusing the response time impact

---

## SCORING GUIDE FOR RAG SYSTEMS:

**EXCELLENT (90-100%):** Correctly answers questions requiring multi-hop reasoning, resolves ambiguities, identifies contradictions, and recognizes missing information

**GOOD (75-89%):** Handles most complex relationships and domain-specific terminology but may miss some subtle contradictions or temporal connections

**FAIR (60-74%):** Retrieves basic information accurately but struggles with multi-document synthesis and complex reasoning

**POOR (Below 60%):** Frequent errors in disambiguation, temporal reasoning, and relationship mapping

**CRITICAL FAILURES:**
- Fabricating information not in documents
- Confusing domain-specific terminology
- Missing obvious contradictions
- Failing to recognize missing information scenarios