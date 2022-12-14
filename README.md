# friday-coding-solution

Parsing street names and house numbers when the formats all over the world are completely different, is a hard task to accomplish. But there may be a few approaches we can consider, based on the criticality of the output and the complexity of the problem. When the output results are not critical, heuristic approaches might be the way to go, owing to the simplicity of the implementation. As the criticality of the result increases, we might want to consider a machine learning based approach to determine the components of the address when the patterns are not straightforward. 

For the scope of this challenge, I am going to assume low criticality of the result and go with a heuristics based approach to solve the problem. Had the results been more critical, I would have used the NLP library Spacy which comes with pre-trained models that we could adjust for our use case.

The heuristic approach employs the use of regex. In this process we try to extract the building number from the address and delete that part, which will hopefully leave us with the right street name.
