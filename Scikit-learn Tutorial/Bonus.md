## 🌟 Speaking of Open Source: How about a bonus assignment?

Throughout the tutorials, a primary goal has been to set you up to become exceptional machine learning engineers by letting you cover more machine learning engineering-related content and exposing you to likewise more specialized assignments than average machine learning students in other universities do. This ought to as well save you time in the future (more than that consumed in the tutorial 😉) by not having you need to learn such concepts or perform extra analysis later yourself.

Here we push this idea a little further.
### 🤔 Problem Statement

- Scikit-learn DOES NOT support the Bayes classifier over arbitrary distributions

     - Only GNB, LDA and QDA (Gaussian assumption)
     
     - Misses out on the most optimal classifier when distribution is not Gaussian

- Likewise, it implements Kernel Density Estimation and Gaussian Mixture Models 

    - But with no way to use them for Bayes classification

### 💡 Proposed Solution

- You to implement a **generic** Bayes Classification library for practitioners that may need it

    - I.e., solves the aforementioned issue of Scikit-learn
    - As TA may show you later, wrapping code in a library is easier than you expect

- There is a probability that another package may exist for this but P is either low or its equivalently unreachable or you can do it better

- Counts as open-source experience and a valuable addition to your portfolio

#### 📃 Conditions For Pursuing the Assignment and Using Lab Code

- Be able to articulate such code as if it was completely authored by you

- Idealize the implementation and design (structure) for production quality

- Be ready to write more tests, more documentation and warnings (easy)

- Perform a sufficient number of transformative changes

#### 🧠 Some Transformative Ideas

- Split the interfaces for better seperation between different genres of the Bayes classifier*

- Parallelize the Gaussian Bayes classifier with einsum, compute only variances for Gaussian Naive Bayes, etc.*

- Be ready to implement Gaussian Mixture Models*

- Parallelize kernel density estimation over many inference points*

- Support more bump functions and custom bump functions in KDE

- Enhance KDE with KNNs and 

- Get creative in general

If you are interested email or contact your TA via Discord. In which case, they may be happy to provide mentorship and guidance, should you need it.

#### 📍 Final Notes

- You can work on this alone or in a pair (or not at all).

- The point of this assignment is not the bonus, it's the experience.