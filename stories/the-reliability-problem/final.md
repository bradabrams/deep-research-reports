# The Reliability Problem

*by Claudia Vance*

---

Output 4847-C.

Tomás had reviewed three hundred and twelve outputs the day everything went wrong, and he'd already forgotten three hundred and eleven of them. This one had crystallized, lodged in his memory like glass in a wound. He sat in the glass-walled conference room on the fourth floor of Meridian Dynamics, facing an HR representative named Clara and a systems analyst named Peters. Outside, the open-plan office stretched like a field of monitors, each station occupied by someone trying very hard not to look up.

"If you could walk us through your review," Clara said. She had a tablet, a stylus, and an expression of concern carefully free of judgment.

Tomás had replayed that morning in his head for seventy-two hours. The code appearing on his screen. The shape of it. The instinctive narrowing of focus on the third nested function.

"I flagged it for rejection," he said. "I thought I saw an error."

"Thought you saw." Peters made a note. "Can you be more specific?"

---

The morning of. Forty-seven hours before this room.

The queue chimed—that soft two-note tone the onboarding materials called "attention-optimized" and that Tomás's colleague Marcus more accurately termed "Pavlovian torture." After eight months on the reliability floor, the sound arrived in his dreams, pulling him to wakefulness at 3 AM to check a screen that wasn't there.

He settled into his station at 8:04 AM, four minutes late because the coffee line had been longer than usual. It shouldn't have mattered—nobody cared about four minutes—but he felt it anyway. The screen woke at his presence. The queue populated. Seventeen outputs waiting from the overnight batch, more arriving in steady pulses as the agent systems churned.

The reliability floor held thirty-four specialists, down from fifty-eight when Tomás started. The AI got better; they needed fewer catchers. Every improvement brought an announcement, a celebration in company Slack: *We're delighted to share that our agent reliability score has increased to 89.3%!* The unspoken corollary: *We'll need three fewer of you.*

Tomás pulled on his haptic gloves, felt them calibrate against his fingertips. A gentle pulse for high-confidence outputs, a sharper buzz for uncertain ones. He liked the texture of knowing the system's doubt in his hands before his eyes found the code.

Output 4844-A appeared. Inventory reconciliation module. Clean structure, standard patterns, confidence score 94.8%. The gloves pulsed soft as a heartbeat. Tomás scanned it, approved it. Green light.

Output 4846-A. Database query handler. Confidence 88.4%. The gloves buzzed sharper. He read more carefully. Something in the error handling felt sparse. He marked it yellow—escalate for secondary review. Let someone else decide.

Then 4847-C arrived.

Supply chain routing function. Confidence 97.2%. The gloves barely registered—a whisper of assurance. High confidence. The system was sure.

But Tomás wasn't.

He read the code. Read it again. The logic was dense but competent, handling the complex problem of optimizing delivery routes across multiple distribution nodes. Nothing obviously wrong. The structure was clean.

And yet.

There was a shape in the third nested function—a way the loop variables were initialized, a particular arrangement of conditionals—that snagged something in his memory. He'd seen this signature before. Eighteen months ago, maybe longer, back when he was still writing code himself. Back when he'd spent three days tracking down a subtle off-by-one error in a pagination module, the satisfaction of finding it so sharp he could still taste it. That bug had hidden behind exactly this shape. Loop variables dancing in exactly this pattern.

The AI's confidence was 97.2%. The system was saying: *I'm almost certain this is right.*

Tomás's gut was saying: *I've seen this before, and it was wrong.*

He had maybe forty seconds. Other outputs were queuing. The chime would sound again. He could approve it—trust the confidence score, the testing layers, the monitoring downstream.

Or he could trust himself.

A small hesitation. The number 97.2% glowing on his screen. Almost certain. But the shape was there, familiar as a face glimpsed across a room, and he couldn't unsee it.

He marked it red.

The system acknowledged: *Output 4847-C flagged for regeneration. Reason: potential loop boundary error.*

Tomás moved to the next output. The queue chimed.

---

Clara shifted in her chair. Three hours into the investigation, and she looked tired. Not bored—there was something in her eyes that might have been sympathy, or dread. "The pattern you described," she said. "Can you explain where you learned to recognize it?"

"When I was a developer." Tomás heard the past tense land heavy. "A specific arrangement of loop variables that used to indicate off-by-one errors. I saw it cause problems multiple times."

"Used to indicate," Peters repeated.

"Yes."

"Are you aware that the agent system underwent significant retraining fourteen months ago specifically to address boundary-condition errors?"

Tomás felt something tighten in his chest. "I knew there were updates. I don't know every detail of what changed."

"The signature you recognized," Peters continued, "was characteristic of outputs prior to version 3.2. The current system, version 4.1, no longer produces that error. In fact, that pattern now typically indicates a deliberate defensive coding choice rather than a bug."

The room went quiet.

"The output you flagged," Peters said, "was correct."

Tomás's stomach dropped. He felt it—the physical sensation of ground giving way, a lurch that started in his chest and spread outward. He gripped the edge of his chair.

"But I—" He stopped. What was there to say?

---

Twenty minutes after flagging. The same station. The same chair.

The regenerated output arrived: 4847-C-R1. The system had taken his rejection, analyzed his stated reason, and produced a new version. It had interpreted his flag as a constraint—*avoid the flagged pattern*—and reshaped its solution accordingly. Tomás had no way of knowing what compromises that reshaping might have introduced.

He reviewed it. The third nested function looked different now—cleaner, he thought. The signature that had snagged his attention was gone. The confidence score had dropped slightly to 96.8%, but that happened sometimes with regenerations, the system second-guessing itself.

He felt a small satisfaction. *See? The system agrees there was something to fix.*

He approved it. Green light.

The regenerated version shipped that evening, bundled into the NorthWest Health Network integration package. Tomás went home, ate leftover pasta, watched two episodes of a show he was already forgetting, and went to bed without dreaming about anything at all.

---

"The regenerated version," Clara said, "contained a race condition."

Tomás had read the incident report. He'd memorized parts of it the way you memorize a wound.

"Under standard load, it functioned correctly," Peters explained. "But during high-throughput conditions—the kind of surge that occurs during emergency redistribution scenarios—the race condition caused route calculations to fail silently. Shipments were assigned to incorrect destinations without triggering error alerts."

Tomás stared at the table.

"Four days after deployment, a winter storm hit the Pacific Northwest. Multiple hospitals activated emergency supply protocols simultaneously. The system processed over twelve thousand routing requests in a ninety-minute window."

"I know."

"Eight hundred and forty-three shipments were misdirected. Insulin, antibiotics, surgical supplies. Some deliveries were delayed by up to eighteen hours."

"I know."

"No one died." Clara's voice softened. "The hospitals had backup protocols. There were close calls—a pediatric diabetes patient in Spokane whose backup supply arrived with twelve minutes to spare—but no one died."

Tomás closed his eyes. Twelve minutes. Twelve minutes between a mistake and a catastrophe. Between a career and a courtroom.

"We're not here to assign blame," Clara said. "We're trying to understand the systemic factors."

*Systemic factors.* He was the systemic factor. Him. His pattern recognition. His experience. The thing that made him valuable had made him dangerous.

---

Dr. Yuki Tanaka entered the room two hours into the review.

She wasn't what Tomás expected. Tall, gray-streaked hair pulled back, glasses that looked like they cost more than his monthly rent. Her hands were steady when she set down her coffee—the steadiness of someone who'd been trained in precision, though Tomás couldn't guess at what. Her title, according to the email invite, was "Human Factors Analyst." A job that hadn't existed two years ago.

"Tomás," she said, sitting down. Not a question.

"Dr. Tanaka."

"I've been reviewing your case. Not to evaluate your performance—to understand how you reached your decision." She had no tablet, no notes. Just attention. "You had a 97.2% confidence score. The system was telling you, with near-certainty, that the output was correct. And you overrode it. Why?"

"Because I'd seen that shape before."

"But you hadn't seen it in recent outputs. Version 4.1 doesn't produce that signature."

"I didn't know that."

"No." She leaned back. "You didn't. You were operating on expertise that had become outdated without any mechanism to signal the shift. The AI changed. Your mental model didn't."

Tomás felt the weight of it. He had been checking for ghosts.

"How was I supposed to know?" he asked.

Dr. Tanaka was quiet for a moment. "You weren't," she said. "That's the problem."

---

Night. His apartment.

The city made its sounds outside—traffic, voices, the distant hum of things happening without him. Tomás sat on his couch in the dark, phone face-down on the cushion beside him. People had been texting. He couldn't look.

He got up. Filled the kettle. Watched the water heat without really seeing it. His hands moved through the familiar motions—mug, tea bag, waiting—while his mind circled the same drain.

94.6% accuracy over eight months. 3.2% false positive rate. 2.2% false negative rate. Better than average. Better than most.

The kettle clicked off. He poured the water, watched it darken.

He'd been good at catching errors. It was the thing he did. When he'd transitioned from developer to reliability specialist—when the writing on the wall became too clear to ignore—he'd told himself it was a lateral move. Different skills. Still valuable.

And he was. Most of the time. The 12% error rate that justified human review was real. He caught real problems.

But he'd also created this one. He had overridden the system's correct judgment with his outdated human judgment, and the regeneration his flag triggered had introduced the bug that misdirected eight hundred and forty-three shipments.

If he hadn't been in the loop, the correct code would have shipped.

The tea grew cold in his hands.

*Is he a safety net or a speed bump?*

The answer was both. At the same time. Inseparable. That was the reliability problem. Not the AI's reliability. His.

---

The park bench was cold through his jeans.

Tomás had called in sick—the first time in eight months. He needed air, something that didn't chime or require decisions. The park near his apartment had a pond with ducks that didn't care about supply chain routing algorithms.

"May I sit?"

He looked up. Dr. Tanaka, in a gray coat, coffee in hand.

"Are you following me?"

"I asked your address from HR." She sat without waiting for permission. "I wanted to talk. Off the record."

"Am I being fired?"

"No. No one's being fired." She sipped her coffee. "The investigation concluded this morning. The finding was system design failure, not human error."

It didn't feel like relief. "They're blaming the system?"

"They're recognizing that human review of high-confidence outputs produces more errors than it catches. The rejection of correct outputs by specialists operating on outdated pattern recognition is a documented failure mode. You're not unique. You're a case study."

"Great."

"They're changing the process. Starting next month, human review will only apply to outputs below 90% confidence. Everything above goes straight to automated testing."

Tomás stared at the ducks. "So I'm redundant."

"No." Dr. Tanaka turned to look at him. "You caught something else."

---

"On the day you flagged 4847-C, you also flagged output 4851-A. Do you remember?"

Tomás searched his memory. He didn't. The day was a blur of chimes and decisions. "I flagged a lot of outputs that day."

"The investigation included a security audit of every output you flagged that week. 4851-A came up immediately." She pulled out her phone. "Data validation module. Confidence score 62.3%. You marked it red. Your reason was 'suspicious authentication bypass pattern.'"

"I don't remember."

"You were right."

Something loosened in Tomás's chest. And tightened. Both at once.

"The original output had a vulnerability that would have allowed unauthorized access to the routing system. Not a misdirection—a full breach. If it had shipped, the entire NorthWest Health Network logistics infrastructure could have been compromised. Patient data. Supply chain access. Facility security systems."

"I don't—" Tomás shook his head. "I don't remember that one at all."

"You reviewed three hundred and twelve outputs that day. Nobody remembers them all." Dr. Tanaka pocketed her phone. "You were right about 4851-A. You were wrong about 4847-C. Same day. Same judgment. Same expertise."

Tomás sat with it. The weight didn't lift; it redistributed.

"There's no way to separate them," he said.

"No."

"I can't take credit for one without taking blame for the other."

"That's correct."

"So what do I do with that?"

Dr. Tanaka was quiet. The ducks moved through the water, oblivious. When she spoke, her voice had changed—softer, the professional distance narrowing.

"I was a pilot. Before this. Twenty years in commercial aviation. The automation transition—" She stopped, shook her head. "Different technology, same questions. When do you trust the system? When do you override? How do you stay sharp when most of the time you're just watching?"

She looked at her hands. Steady hands. Trained hands.

"I made a decision once. Overrode an automated system because something felt wrong. I was right. Saved one hundred and forty-three people."

Tomás waited. He could feel there was more.

"The next year, I overrode another system. Same instinct. Same certainty." She met his eyes. "I was wrong. Nothing catastrophic—we landed fine, passengers didn't even know. But I knew. And I spent the next decade wondering which version of me was real. The one who saved people, or the one who almost hurt them."

"What did you decide?"

"Both. That's the human condition, Mr. Reyes. We're the variable in the system that can't be optimized. The irreducible uncertainty." She stood, brushing off her coat. "It's also why they still need us. For now."

Tomás stayed on the bench after she left. The ducks circled. The cold seeped through his jeans. He could go home. He could update his resume. He could call his mother, who still didn't understand what he did for a living.

Instead, he just sat. Letting the weight redistribute. Letting it settle somewhere he could carry it.

---

One month later. The reliability floor.

It was quieter now. Nineteen specialists where there had been thirty-four. The queue was smaller—only low-confidence outputs, the stuff the system was actually uncertain about. The high-confidence work flowed past without human eyes, straight to automated testing and deployment.

Tomás's station felt the same. Same chair, same screen, same gloves. But the rhythm had changed. Fewer chimes. More silence between. More time to think—which wasn't always better.

He'd thought about leaving. Had the conversation with himself a dozen times. But something Dr. Tanaka said kept surfacing: *the irreducible uncertainty.* They still needed someone in the loop, even if the loop was smaller now. Even if the value proposition had narrowed.

The chime sounded.

An output appeared on his screen. Data processing module, confidence score 71.4%. The gloves buzzed soft and uncertain against his fingertips. The system wasn't sure. That was why it was asking.

Tomás read the code. Looked at the structure, the patterns, the logic. Something in the error handling caught his attention—a shape that reminded him of something he'd seen before.

He didn't know if his instinct was right. Didn't know if the pattern he recognized was current or obsolete, valid or ghostly. He might catch a real error. He might create a new one. There was no way to know in advance, no way to separate the catches from the misses until the consequences unfolded downstream.

He knew only that he was here, in the loop, and a decision was required.

He made one.

The chime sounded again. Another output, waiting. Another decision that might matter, might not, probably wouldn't but possibly could.

Tomás moved to the next one.

---

*The End*
