

def as_text(text):

   from fastcoref import spacy_component
   import spacy

   nlp = spacy.load("en_core_web_sm")
   nlp.add_pipe("fastcoref")

   doc = nlp(text)
   print("Coreference Clusters:")
   print(doc._.coref_clusters)

   doc = nlp(text, component_cfg={"fastcoref": {'resolve_text': True}})
   print("\nResolved Text:")
   print(doc._.resolved_text)


#############################################################################################################

def as_clusters(text):

   from fastcoref import FCoref

   model = FCoref(device='cpu')

   preds = model.predict(texts=[text])

   print(preds[0].get_clusters(as_strings=False))

   print(preds[0].get_clusters())

   print(preds[0].get_logit(span_i=(0, 4), span_j=(30, 33)))


if __name__ == "__main__":
   text = 'John went to the park to meet his friend, Sarah. ' \
          'She had been waiting for him near the fountain. ' \
          'When he arrived, he waved to her, and she smiled back. ' \
          'They decided to walk around and talk about their plans for the weekend. ' \
          'John mentioned that he wanted to visit the new museum, and Sarah thought it was a great idea. ' \
          'As they walked, Sarah pointed out a group of ducks by the pond. ' \
          '"Look at them!" she exclaimed. ' \
          'John laughed and took a picture of the ducks to show his sister later. ' \
          'He told Sarah that his sister loves animals and would enjoy seeing the photo. ' \
          'After spending some more time at the park, they said goodbye and promised to meet again soon. ' \
          'John felt happy about the day, and so did Sarah.'

   as_text(text)
   as_clusters(text)