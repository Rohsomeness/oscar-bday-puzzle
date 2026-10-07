# Oscar's 28th birthday puzzle

A one-page puzzle for Oscar, built the same way as [veet-bday-puzzle](https://github.com/Rohsomeness/veet-bday-puzzle). Each clue is a photo, a video, or just a question. The answer is stored as a SHA-256 hash, so it is not written in the page.

Three clues are in so far. `GIFT_MESSAGE` is still a stand-in.

## Add a clue

1. Put the photo or video in `images/`. A clue can also be text only.
2. Hash the answer exactly as it should be typed:

   ```bash
   python3 scripts/hash_answer.py "the answer"
   ```

   The script trims and lowercases first, which is what the page does too.
3. Add an entry to the `puzzles` array in `index.html`:

   ```js
   {
     type: "image", // "video" for a video. Omit src for a text-only clue.
     src: "images/1.jpg",
     question: "What year was this taken?",
     answerHash: "<paste the hash>",
   }
   ```

   `answerHashes` can be a list when more than one wording should pass.

GitHub rejects files over 100MB. Keep videos under that.

## The last page

`GIFT_MESSAGE` in `index.html` is what shows after the last correct answer. It is a stand-in until the real gift is set.

## Run it

Answers are checked with `crypto.subtle`, which does not work from a `file://` link. Serve the folder:

```bash
python3 -m http.server
```

Then open `http://localhost:8000`.

The live site is [rohsomeness.github.io/oscar-bday-puzzle](https://rohsomeness.github.io/oscar-bday-puzzle/).

Progress is saved in `localStorage` under `oscar-bday-puzzle`. It resets when the number of clues changes. Clear that key to start over.
