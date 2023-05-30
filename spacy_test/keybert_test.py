from keybert import KeyBERT

doc = """
         Abstract The ability to perform in-hand manipulation
        still remains an unsolved problem; having this capability
        would allow robots to perform sophisticated tasks requiring
        repositioning and reorienting of grasped objects. In this work,
        we present a novel non-anthropomorphic robot grasper with
        the ability to manipulate objects by means of active surfaces at
        the ngertips. Active surfaces are achieved by spherical rolling
        ngertips with two degrees of freedom (DoF)  a pivoting
        motion for surface reorientation  and a continuous rolling
        motion for moving the object. A further DoF is in the base
        of each nger, allowing the ngers to grasp objects over a
        range of size and shapes. Instantaneous kinematics was derived
        and objects were successfully manipulated both with a custom
        handcrafted control scheme as well as one learned through
        imitation learning,
        in simulation and experimentally on the
        hardware.
      """
kw_model = KeyBERT()
keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None, highlight=True)

print(keywords)