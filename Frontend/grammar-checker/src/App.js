import React, { useState } from "react";
import axios from "axios";

const teamMembers = [
  {
    name: "Benaiah Saju Joseph",
    id: "21BRS1300",
  },
  {
    name: "Achintya Singh",
    id: "21BRS1352",
  },
  {
    name: "Utkarsh Raghav",
    id: "21BRS1342",
  },
  {
    name: "Vishnu Sujith Kurup",
    id: "21BRS1588",
  },
 
];

function SentenceChecker() {
  const [sentence, setSentence] = useState("");
  const [highlightedParagraph, setHighlightedParagraph] = useState(null);
  const [correctedParagraph, setCorrectedParagraph] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:5000/check", {
        sentence: sentence,
      });
      const result = response.data;

      if (result.prediction === "Correct") {
        // Highlight entire paragraph in green as a raw HTML string
        const greenParagraph = `<span class="text-green-600">${sentence}</span>`;
        setHighlightedParagraph(greenParagraph);
        setCorrectedParagraph(greenParagraph);
      } else {
        // Display highlighted errors in red on the left and the corrected paragraph in green on the right
        const redParagraph = `<span class="text-red-600">${sentence}</span>`;
        const greenCorrectedParagraph = `<span class="text-green-600">${result.corrected_paragraph}</span>`;
        setHighlightedParagraph(redParagraph);
        setCorrectedParagraph(greenCorrectedParagraph);
      }
    } catch (error) {
      console.error("Error fetching data", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-500 to-purple-700 p-4 relative">
      <div className="fixed left-0 top-0 w-64 h-full p-4 overflow-hidden flex flex-col justify-center items-center">
        <h2 className="text-xl font-bold text-white mb-4">Team Members</h2>
        <div className="flex flex-col items-center space-y-4">
          {teamMembers.map((member, index) => (
            <div
              key={index}
              className="bg-white rounded-lg p-4 shadow-lg transition-transform transform animate-float"
            >
              <h3 className="text-lg font-bold">{member.name}</h3>
              <p className="text-sm text-gray-1000">{member.id}</p>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-white shadow-lg rounded-lg p-8 max-w-2xl w-full flex flex-col justify-center items-center z-10">
        <h1 className="text-4xl font-extrabold text-gray-800 text-center mb-6">
          Malayalam Grammar Checker
        </h1>

        <form onSubmit={handleSubmit} className="w-full space-y-6">
          <textarea
            className="w-full p-4 border-2 border-gray-300 rounded-lg shadow-md focus:outline-none focus:ring-4 focus:ring-blue-500 focus:border-transparent"
            rows="5"
            placeholder="Enter your paragraph here..."
            value={sentence}
            onChange={(e) => setSentence(e.target.value)}
            required
          ></textarea>

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-3 rounded-lg font-bold hover:bg-blue-700 transition-colors duration-300 shadow-md"
          >
            {loading ? "Checking..." : "Check Paragraph"}
          </button>
        </form>

        {/* Display highlighted and corrected paragraphs side by side */}
        {highlightedParagraph && correctedParagraph && (
          <div className="mt-8 w-full flex flex-row space-x-4">
            {/* Highlighted Paragraph */}
            <div className="bg-white p-4 rounded-lg shadow-md w-1/2">
              <h3 className="text-lg font-semibold mb-2">Highlighted Errors:</h3>
              <p
                className="text-gray-800"
                dangerouslySetInnerHTML={{ __html: highlightedParagraph }}
              />
            </div>

            {/* Corrected Paragraph */}
            <div className="bg-white p-4 rounded-lg shadow-md w-1/2">
              <h3 className="text-lg font-semibold mb-2">Corrected Paragraph:</h3>
              <p
                className="text-gray-800"
                dangerouslySetInnerHTML={{ __html: correctedParagraph }}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default SentenceChecker;
