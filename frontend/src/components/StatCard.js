export default function StatCard({ title, value, icon, color, testId }) {
  const colorClasses = {
    gold: "text-mir-gold shadow-[0_0_15px_rgba(255,215,0,0.15)]",
    blue: "text-mir-blue shadow-[0_0_15px_rgba(0,122,255,0.15)]",
    green: "text-green-400 shadow-[0_0_15px_rgba(16,185,129,0.15)]",
    red: "text-mir-red shadow-[0_0_15px_rgba(255,59,48,0.15)]"
  };

  return (
    <div
      className={`bg-mir-charcoal border border-white/5 rounded-xl p-6 shadow-xl hover:border-mir-gold/30 hover:shadow-2xl transition-all duration-300 group ${colorClasses[color]}`}
      data-testid={testId}
    >
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <p className="text-xs font-secondary font-medium tracking-widest uppercase text-slate-500 mb-2">
            {title}
          </p>
          <p className="text-3xl font-mono font-bold text-white" data-testid={`${testId}-value`}>
            {value}
          </p>
        </div>
        <div className={`p-3 rounded-lg bg-white/5 group-hover:bg-white/10 transition-colors`}>
          {icon}
        </div>
      </div>
    </div>
  );
}
