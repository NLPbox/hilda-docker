# hilda-docker

This docker container allows you to build, install and run the HILDA
RST discourse parser (Hernault et al. 2010) in a docker container.

## Obtaining HILDA

The HILDA parser is available without pay for academic research, but it
can't be downloaded directly. You'll need to sign a license agreement first.
Please contact [Prof. Helmut Prendinger](http://research.nii.ac.jp/~prendinger/).

## Building HILDA

```
git clone https://github.com/nlpbox/hilda-docker
cp hilda_0.9.5_full.tar.gz hilda-docker/
cd hilda-docker
docker build -t hilda .
```

## Running HILDA

To test if parser works, just run ``docker run -ti hilda``.
To run the parser on the file ``/tmp/input.txt`` on your
local machine, run:

```
docker run -v /tmp:/tmp -ti hilda /tmp/input.txt
```

The input files should be encoded in UTF-8. Each sentence ending must
be marked with ``<s>`` and each paragraph ending with ``<p>``.

## Example Input

```
Henryk Szeryng (22 September 1918 - 8 March 1988) was a violin virtuoso
of Polish and Jewish heritage.<p>

He was born in Zelazowa Wola, Poland.<s> Henryk started piano and
harmony training with his mother when he was 5, and at age 7 turned to
the violin, receiving instruction from Maurice Frenkel.<s> After
studies with Carl Flesch in Berlin (1929-32), he went to Paris to
continue his training with Jacques Thibaud at the Conservatory,
graduating with a premier prix in 1937.<p>

He made his solo debut in 1933 playing the Brahms Violin Concerto.<s>
From 1933 to 1939 he studied composition in Paris with Nadia Boulanger,
and during World War II he worked as an interpreter for the Polish
government in exile (Szeryng was fluent in seven languages) and gave
concerts for Allied troops all over the world.<s> During one of these
concerts in Mexico City he received an offer to take over the string
department of the university there.<p>

In 1946, he became a naturalized citizen of Mexico.<p>

Szeryng subsequently focused on teaching before resuming his concert
career in 1954.<s> His debut in New York City brought him great
acclaim, and he toured widely for the rest of his life.<s> He died in
Kassel.<p>

Szeryng made a number of recordings, including two of the complete
sonatas and partitas for violin by Johann Sebastian Bach, and several
of sonatas of Beethoven and Brahms with the pianist Arthur
Rubinstein.<s> He also composed; his works include a number of violin
concertos and pieces of chamber music.<p>

He owned the Del Gesu "Le Duc", the Stradivarius "King David" as well
as the Messiah Strad copy by Jean-Baptiste Vuillaume which he gave to
Prince Rainier III of Monaco.<s> The "Le Duc" was the instrument on
which he performed and recorded mostly, while the latter ("King David"
Strad) was donated to the State of Israel.<p>
```

## Example Output

```
(Elaboration[N][S]
  (Joint[N][N]
    (Elaboration[N][S]
      Henryk Szeryng ( 22 September 1918 - 8 March 1988 )
      was a violin virtuoso of Polish and Jewish heritage .)
    (Joint[N][N]
      (Joint[N][N]
        He was born in Zelazowa Wola , Poland .
        (Joint[N][N]
          (Background[N][S]
            Henryk started piano and harmony training with his mother
            when he was 5 ,)
          and at age 7 turned to the violin ,))
      (Joint[N][N]
        (Elaboration[N][S]
          receiving instruction from Maurice Frenkel .
          (Temporal[S][N]
            (Elaboration[N][S]
              After studies with Carl Flesch in Berlin
              ( 1929-32 ) ,)
            (Elaboration[N][S]
              he went to Paris to continue his training with Jacques Thibaud at the Conservatory ,
              graduating with a premier prix in 1937 .)))
        (Joint[N][N]
          (Elaboration[N][S]
            He made his solo debut in 1933
            playing the Brahms Violin Concerto .)
          (Joint[N][N]
            From 1933 to 1939 he studied composition in Paris with Nadia Boulanger ,
            (Joint[N][N]
              (Elaboration[N][S]
                and during World War II he worked as an interpreter for the Polish government in exile
                ( Szeryng was fluent in seven languages ))
              (Elaboration[N][S]
                and gave concerts for Allied troops all over the world .
                During one of these concerts in Mexico City he received an offer to take over the string department of the university there .)))))))
  (Elaboration[N][S]
    (Elaboration[N][S]
      (Joint[N][N]
        (Attribution[N][S]
          In 1946 ,
          he became a naturalized citizen of Mexico .)
        (Elaboration[N][S]
          Szeryng subsequently focused on teaching before resuming his concert career in 1954 .
          (Joint[N][N]
            His debut in New York City brought him great acclaim ,
            (Elaboration[N][S]
              and he toured widely for the rest of his life .
              (Attribution[S][N] He died in Kassel .)))))
      (Elaboration[N][S]
        (Elaboration[N][S]
          (Elaboration[N][S]
            Szeryng made a number of recordings ,
            including two of the complete sonatas and partitas for violin by Johann Sebastian Bach , and several of sonatas of Beethoven and Brahms with the pianist Arthur Rubinstein .)
          He also composed ;)
        his works include a number of violin concertos and pieces of chamber music .))
    (Elaboration[N][S]
      He owned the Del Gesu `` Le Duc '' , the Stradivarius `` King David '' as well as the Messiah Strad copy by Jean-Baptiste Vuillaume
      (Attribution[S][N]
        which he gave to Prince Rainier III of Monaco .
        (Elaboration[N][S]
          The `` Le Duc '' was the instrument
          (Contrast[N][N]
            on which he performed and recorded mostly ,
            (Elaboration[N][S]
              (same-unit[N][N]
                (Elaboration[N][S]
                  while the latter
                  ( `` King David '')
                Strad ))
              was donated to the State of Israel .)))))))
```

# Citation

Hernault, H., Prendinger, H., DuVerle, D. A., Ishizuka, M., & Paek, T. (2010).
[HILDA: a discourse parser using support vector machine classification](http://journals.linguisticsociety.org/elanguage/dad/article/download/591/591-2300-1-PB.pdf). Dialogue and Discourse, 1(3), 1-33.
