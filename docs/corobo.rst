Using cvbot
============

GitHub/GitLab utilities
-----------------------

1. Getting invitation to the GitHub org:
   Send ``Hello World`` in the chat room.
2. Want to work on an issue, first assign yourself:
   ``cvbot assign <issue-link>``
3. Assigned issue is time-consuming, no longer interesting? Wanna discontinue:
   ``cvbot unassign <issue-link>``
4. Wanna file a new issue, but don't want to leave gitter?:
   ``cvbot new issue <repo> <title>\n[description\n]+``
5. Mark a PR as a work-in-progress
   ``cvbot mark wip <pr-link>``
6. Your PR was marked WIP, you did the changes and want it be reviewed again?
   Add ``pending_review`` label:
   ``cvbot mark pending <pr-link>``

cloudcv utilities
---------------

1. Wanna know stats regarding cloudcv?:

   a. Get user contribution stats using:
      .. code::
         >> cvbot contrib stats <user>
         User <user> has:
         1. Opened x issues
         2. Commited 17 commits
         3. Done 61 reviews.
   b. Bear stats(all languages):
      .. code::
         >> cvbot bear stats
         There are total x bears.
   c. Bear stats(particular languages):
      .. code::
         >> cvbot bear stats python
         There are 17 bears for python language
   d. Language stats:
      .. code::
         >> cvbot lang stats
         cloudcv supports 63 languages.
   e. stats(both bear and lang stats(for summary stats)):
      .. code::
         >> cvbot stats
         cloudcv has 102 bears across 63 languages.
2. List bears of particular languages:
   .. code::
      >> cvbot ls bears python ...
        Bears for python are:
        | BanditBear | CPDBear | MypyBear | PEP8Bear | PEP8NotebookBear | PyCommentedCodeBear | PyDocStyleBear
        | PyFlakesBear | PyImportSortBear | PyLintBear | PyUnusedCodeBear | PycodestyleBear | PyromaBear
        | PythonPackageInitBear | RadonBear | VultureBear | YapfBear |
3. Run cloudcv from chat itself!
   .. code::
      cvbot run Bear1 setting1=1 setting2=2 Bear2
      ```
      import this
      this = 3
      some = 'code'
      ```

Answer
------

You have got a question, no one's available to answer. Let cvbot try to answer
it for you:
``cvbot answer your question string goes here``

The scope of questions that cvbot can answer is limited to what is present in
api(https://api.cloudcv.io) and user(https://docs.cloudcv.io) docs.

Misc.
-----

1. Someone is asking a googlable question? Respond with a lmgtfy:
   ``cvbot lmgtfy this is the search string``
2. Get bot to apologize:
   ``cvbot nm``
3. Explain pre-defined terms:
   ``cvbot explain rebase``
4. Is your PR ready to merge, go shipit!
   ``cvbot ship it``
5. Ask a question to wolfram knowledge engine:
   ``cvbot wa question/query string``
